import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from textwrap import wrap

# Register Arial Font
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

# Constants for PDF layout
LEFT_MARGIN = 72
RIGHT_MARGIN = 72
TOP_MARGIN = 72
BOTTOM_MARGIN = 72
PAGE_WIDTH = 595
PAGE_HEIGHT = 842
FONT_SIZE = 12
LINE_SPACING = 14
CHAR_WIDTH_ESTIMATE = 6

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText() + '\n'
    return text

def create_pdf_with_text(text, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=A4)
    c.setFont("Arial", FONT_SIZE)

    max_char_per_line = (PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN) // CHAR_WIDTH_ESTIMATE
    y = PAGE_HEIGHT - TOP_MARGIN

    paragraphs = text.split('\n')
    for paragraph in paragraphs:
        lines = wrap(paragraph, max_char_per_line, replace_whitespace=False, drop_whitespace=True)
        for line in lines:
            if y < BOTTOM_MARGIN:
                c.showPage()
                c.setFont("Arial", FONT_SIZE)
                y = PAGE_HEIGHT - TOP_MARGIN
            c.drawString(LEFT_MARGIN, y, line)
            y -= LINE_SPACING

        # Check if there are subsequent paragraphs and add extra space if true
        if paragraph != paragraphs[-1]:
            y -= LINE_SPACING

        # Check for a new page if y goes below the bottom margin
        if y < BOTTOM_MARGIN:
            c.showPage()
            c.setFont("Arial", FONT_SIZE)
            y = PAGE_HEIGHT - TOP_MARGIN

    c.save()