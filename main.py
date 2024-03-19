from text_processing import tool_selector
from pdf_reader import extract_text_from_pdf

def main():

    tool = "key_points"
    # Options:
    # "summarise"
    # "key_points"
    # "latex"
    # "query"
    # "edit_json"

    processor_tool = tool_selector(tool)

    input_type = "pdf"
    # Options:
    # "text"
    # "pdf"

    pdf_path = r"insert\pdf\path\to\test.pdf"

    if input_type == "text":
        text = input("Enter the text to be processed:\n")
        result = processor_tool.response(text)

    elif input_type == "pdf":
        print("Extracting text from PDF.")
        text = extract_text_from_pdf(pdf_path)
        result = processor_tool.response(text)
        output_filename = f"output/{tool}_" + pdf_path.split("\\")[-1].split(".")[0] + ".txt"
        with open(output_filename, "w") as file:
            file.write(result)

    print("Result:")
    print(result)

if __name__ == "__main__":
    main()