from text_processing import OpenAITextProcessor
import json

class JSON_Editor(OpenAITextProcessor):
    def json_response(self, text, json_content):
        system_message = "You are an expert at digital communications."
        user_message = f"Alter the following JSON entry to match the following description:\n\nDescription:\n{text}\n\nJSON:{json_content}"
        response = self._create_response(system_message, user_message)
        return response

def json_editor():
    json_path = "descriptors_cub.json"
    json_output_path = "descriptors_cub_new.json"

    text = "Create 4-7 visual descriptors of the named bird that attempts to uniquely describe that bird as compared to others within its species, as well as a couple of general descriptors that may relate to the species. Return the output with the original formatting as this is for use in an existing machine learning classification task. "

    # Loop through each entry in the JSON file, calling the json_response method for each entry
    with open(json_path, "r") as file:
        json_content = json.load(file)
    i = 0
    for key in json_content:
        i += 1
        response = JSON_Editor().json_response(text, key)
        json_content[key] = response
        if i >= 10:
            break
        with open(json_output_path, "w") as file:
            json.dump(json_content, file, indent=4)

json_editor()