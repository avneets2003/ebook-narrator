import os
from PyPDF2 import PdfReader

def pdf_to_text(pdf_path):
    if not os.path.isfile(pdf_path):
        print(f"Error: The file '{pdf_path}' does not exist.")
        return
    
    output_dir = os.path.join(os.path.dirname(pdf_path), '.temp')
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_txt = os.path.join(output_dir, os.path.splitext(os.path.basename(pdf_path))[0] + '.txt')

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
    
    os.remove(pdf_path)
    return output_txt
