from text_processing import tool_selector
from pdf_reader import extract_text_from_pdf

def main():

    tool = "summarise"
    # Options:
    # "summarise"
    # "key_points"
    # "latex"
    # "query"

    input_type = "text"
    # Options:
    # "text"
    # "pdf"

    pdf_path = r"\insert\pdf\path\here"

    if input_type == "text":
        text = input("Enter the text to be processed:\n")
    elif input_type == "pdf":
        text = extract_text_from_pdf(pdf_path)

    processor_tool = tool_selector(tool)

    result = processor_tool.response(text)

    print("Processed Result:")
    print(result)

if __name__ == "__main__":
    main()