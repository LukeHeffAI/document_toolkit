import openai
import os

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Base class for handling different types of OpenAI text operations
class OpenAITextProcessor:
    def __init__(self, model="gpt-4-0125-preview", max_tokens=300):
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
    def extract_key_points(self, text):
        system_message = "You are an expert at digital communications."
        user_message = f"Summarise 3-5 main key points of the following text:\n\n{text}"
        return self._create_response(system_message, user_message)
    
class TextSummariser(OpenAITextProcessor):
    def summarise_text(self, text):
        system_message = "You are an expert at technical communication."
        user_message = f"Summarise the following text:\n\n{text}"
        return self._create_response(system_message, user_message)

class TextQuery(OpenAITextProcessor):
    def answer_query(self, text, question):
        system_message = "You are an expert at technical communication."
        user_message = f"Answer the following question about the following text:\n\nQuestion: {question}\n\nText:{text}"
        return self._create_response(system_message, user_message)

class LaTeXFormatter(OpenAITextProcessor):
    def format_text(self, text):
        system_message = "You are an expert at digital communications."
        user_message = f"Format the following text (which has been extracted from a PDF) into an A4 LaTeX document. Do not alter the content:\n\n{text}"
        return self._create_response(system_message, user_message)
