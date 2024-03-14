from text_processing import TextSummariser, KeyPointsExtractor, TextQuery, LaTeXFormatter

def main():
    print("Welcome to the OpenAI Text Processor Interface!")
    print("Please enter your text:")
    user_text = input("> ")

    print("\nSelect the type of processing you want to perform:")
    print("1. Summarise your text.")
    print("2. Extract key points")
    print("3. Draft text in LaTeX")
    print("4. Have a Q&A related to the text")
    choice = input("> ")

    # Instantiate the required class based on user input
    if choice == '1':
        processor = TextSummariser()
        result = processor.summarise_text(user_text)
    elif choice == '2':
        processor = KeyPointsExtractor()
        result = processor.extract_key_points(user_text)
    elif choice == '3':
        processor = LaTeXFormatter()
        result = processor.format_text(user_text)
    elif choice == '4':
        print("\nEnter your query:")
        query = input("> ")
        processor = TextQuery()
        result = processor.answer_query(user_text, query)
    else:
        print("Invalid option. Exiting.")
        return

    print("\nProcessed Result:")
    print(result)

if __name__ == "__main__":
    main()
