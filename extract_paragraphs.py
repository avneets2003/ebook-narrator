import os
import cohere
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('COHERE_API_KEY')

co = cohere.ClientV2(api_key=api_key)

def extract_paragraphs(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    message = f"Without making any comments or paraphrasing, remove unnecessary whitespace characters (including newline characters) from the following text:\n\n{file_content}"

    response = co.chat(
        model="command-r-plus-08-2024",
        messages=[{"role": "user", "content": message}]
    )

    corrected_text = response.message.content[0].text

    with open(file_path, 'w') as file:
        file.write(corrected_text)
