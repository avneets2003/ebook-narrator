import re

def clean_text(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    text = file_content.replace('\n', ' ').replace('\r', ' ')
    text = re.sub(r'\s+', ' ', text)
    
    with open(file_path, 'w') as file:
        file.write(text.strip())
