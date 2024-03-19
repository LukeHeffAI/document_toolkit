from text_processing import OpenAITextProcessor

class JSON_Editor(OpenAITextProcessor):
    def response(self, text, json_content):
        system_message = "You are an expert at digital communications."
        user_message = f"Alter the following JSON entry to match the following description:\n\nDescription:\n{text}\n\nJSON:{json_content}"
        response = self._create_response(system_message, user_message)
        return response

def main():
    json_path = "descriptors_cub.json"

    text = "The current JSON has dot points visually describing each bird species, but they are often not unique to that bird. Remove the existing dot points. Create 4-7 visual descriptors of each bird type that attempts to uniquely describe that bird as compared to others within its species, as well as a couple of general descriptors. Return the output with the original formatting as this is for use in an existing machine learning classification task. "

    # Loop through each entry in the JSON file, calling the response method for each entry
    with open(json_path, "r") as file:
        for line in file:
            print(line)


    # result = JSONEditor().response(text, json_path)

if __name__ == "__main__":
    main()