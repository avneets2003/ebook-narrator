import os
import shutil
from select_file import select_file
from split_pdf import split_and_merge_pdf
from pdf_to_txt import pdf_to_text
from extract_paragraphs import extract_paragraphs
from clean_text import clean_text
from tts import narrate_text

def main():
    file_name = select_file()
    start_page = int(input("Enter the start page: "))
    end_page = int(input("Enter the end page: "))

    if start_page < 1 or end_page < start_page:
        print("Invalid page range. Please ensure start page is less than or equal to end page.")
        return
    
    merged_pdf_file = split_and_merge_pdf(file_name, start_page, end_page)
    txt_file = pdf_to_text(merged_pdf_file)
    extract_paragraphs(txt_file)
    # clean_text(txt_file)
    narrate_text(txt_file)
    temp_dir = os.path.dirname(txt_file)

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
