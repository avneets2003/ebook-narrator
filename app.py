import os
import shutil
from select_file import select_file
from split_pdf import split_and_merge_pdf
from pdf_to_txt import pdf_to_text
from extract_paragraphs import clean_text_with_timer
from tts import narrate_text

CONFIG_FILE = "config.txt"

def load_config():
    start_page = 1
    end_page = 1
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            for line in f:
                if line.startswith("START_PAGE="):
                    try:
                        start_page = int(line.strip().split("=")[1])
                    except ValueError:
                        pass
                elif line.startswith("END_PAGE="):
                    try:
                        end_page = int(line.strip().split("=")[1])
                    except ValueError:
                        pass
    return start_page, end_page

def save_config(start_page, end_page):
    with open(CONFIG_FILE, 'w') as f:
        f.write(f"START_PAGE={start_page}\n")
        f.write(f"END_PAGE={end_page}\n")

def main():
    file_name = select_file()
    saved_start, saved_end = load_config()

    try:
        start_input = input(f"Enter the start page ({saved_start}): ").strip()
        end_input = input(f"Enter the end page ({saved_end}): ").strip()

        start_page = int(start_input) if start_input else saved_start
        end_page = int(end_input) if end_input else saved_end
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if start_page < 1 or end_page < start_page:
        print("Invalid page range. Please ensure start page is less than or equal to end page.")
        return
    
    merged_pdf_file = split_and_merge_pdf(file_name, start_page, end_page)
    txt_file = pdf_to_text(merged_pdf_file)
    clean_text_with_timer(txt_file)
    narrate_text(txt_file)
    temp_dir = os.path.dirname(txt_file)

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

    save_config(end_page + 1, end_page + 1)

if __name__ == "__main__":
    main()
