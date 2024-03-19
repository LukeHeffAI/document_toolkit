import openai
import os
from dotenv import load_dotenv

# Get the API key from the .env file using the dotenv api_key = package
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

max_tokens = 4096

# Base class for handling different types of OpenAI text operations
class OpenAITextProcessor:
    def __init__(self, model="gpt-4-0125-preview", max_tokens=max_tokens):
        self.model = model
        self.max_tokens = max_tokens
    
    def _create_response(self, system_content, user_content):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ],
            temperature=1,
            max_tokens=self.max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response['choices'][0]['message']['content']

class KeyPointsExtractor(OpenAITextProcessor):
    def response(self, text):
        system_message = "You are an expert at digital communications."
        user_message = f"Summarise 3-5 main key points of the following text:\n\n{text}"
        return self._create_response(system_message, user_message)
    
class TextSummariser(OpenAITextProcessor):
    def response(self, text):
        system_message = "You are an expert at technical communication."
        user_message = f"Summarise the following text:\n\n{text}"
        return self._create_response(system_message, user_message)

class TextQuery(OpenAITextProcessor):
    def response(self, text, question):
        system_message = "You are an expert at technical communication."
        user_message = f"Answer the following question about the following text:\n\nQuestion: {question}\n\nText:{text}"
        return self._create_response(system_message, user_message)

class LaTeXFormatter(OpenAITextProcessor):
    def response(self, text):
        system_message = "You are an expert at digital communications."
        user_message = f"Format the following text (which has been extracted from a PDF) into an A4 LaTeX document. Do not alter the content:\n\n{text}"
        return self._create_response(system_message, user_message)
    
class JSONEditor(OpenAITextProcessor):
    def response(self, text, json_path=input("Enter the JSON file path: ")):
        with open(json_path, "r") as file:
            json_content = file.read()
        system_message = "You are an expert at digital communications."
        user_message = f"Alter the following JSON to match the following description:\n\nDescription:\n{text}\n\nJSON:{json_content}"
        response = self._create_response(system_message, user_message)
        json_output_path = json_path.split(".")[0] + "_new.json"
        with open(json_output_path, "w") as file:
            file.write(response)
        return response
    
def tool_selector(tool):
    if tool == "summarise":
        return TextSummariser()
    elif tool == "key_points":
        return KeyPointsExtractor()
    elif tool == "latex":
        return LaTeXFormatter()
    elif tool == "query":
        return TextQuery()
    elif tool == "edit_json":
        return JSONEditor()
    else:
        raise ValueError("Invalid tool selected")