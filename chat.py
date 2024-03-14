import openai
import os
from pdf_reader import extract_text_from_pdf

openai.api_key = os.getenv("OPENAI_API_KEY")

max_tokens = 300

def gen_pod_script(text, max_tokens=max_tokens, speaker_count=1):
    text: str
    max_tokens: int
    speaker_count: int

    if speaker_count == 1:
        response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a talented, intelligent, and creative podcast producer and writer, experienced with writing for the most popular and engaging scientific podcasts. You know your audience are also intelligent, but looking to be entertained and may not be from the field covered in your podcast."},
            {"role": "user", "content": "Read the content of the following text and write a podcast script for a technical audience, with a charismatic host discussing the key points of the text.\n\n{}".format(text)}
        ],
        temperature=1,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    else:
        response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a talented, intelligent, and creative podcast producer and writer, experienced with writing for the most popular and engaging scientific podcasts. You know your audience are also intelligent, but looking to be entertained and may not be from the field covered in your podcast."},
            {"role": "user", "content": "Read the content of the following text and write a podcast script for a technical audience, with a charismatic host interviewing the author of the text, each discussing their interests in the key points of the text. As the script will be input to a speech-to-text model, the lines must be tagged explicitly in-line with <host> and <guest 1>, <guest 2>, etc respectively for {} guests.\n\n{}".format(text, speaker_count)}
        ],
        temperature=1,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    return response['choices'][0]['message']['content']

def LaTeX_format(text, max_tokens=max_tokens):
    '''
    Format cluttered text to be inserted into a PDF file.
    '''
    text: str
    max_tokens: int

    response = openai.ChatCompletion.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": "You are an expert at digital communications."},
        {"role": "user", "content": "Format the following text (which has been extracted from a PDF) into an A4 LaTeX document. Do not alter the content:\n\n{}".format(text)}
    ],
    temperature=0.4,
    max_tokens=max_tokens,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response['choices'][0]['message']['content']

def key_points(text, max_tokens=max_tokens):
    '''
    Summarise the key points of a body of text.
    '''

    text: str
    max_tokens: int

    response = openai.ChatCompletion.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": "You are an expert at digital communications."},
        {"role": "user", "content": "Summarise 3-5 main key points of the following text:\n\n{}".format(text)}
    ],
    temperature=0.5,
    max_tokens=max_tokens,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    key_points = response['choices'][0]['message']['content']

    return key_points

def query(text, max_tokens=max_tokens):
    '''
    Query a body of text.
    '''

    question = input("Enter a question about the text.\n")

    text: str
    max_tokens: int

    response = openai.ChatCompletion.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": "You are an expert at technical communication."},
        {"role": "user", "content": "Answer the following question about the following text:\n\nQuestion: {}\n\nText:{}".format(question, text)}
    ],
    temperature=0.5,
    max_tokens=max_tokens,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    answer = response['choices'][0]['message']['content']

    return answer

def main():
    text = extract_text_from_pdf(r"C:\Users\Luke-\Downloads\2312.01998.pdf")
    answer_text = query(text, max_tokens=500)
    print(answer_text)

if main():
    main()
