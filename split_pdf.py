import os
import shutil
from PyPDF2 import PdfWriter, PdfReader, PdfMerger

def split_pdf(file_name, start_page, end_page):
    if not os.path.isfile(file_name):
        print(f"The file {file_name} does not exist.")
        return

    input_pdf = PdfReader(open(file_name, "rb"))
    base_name = os.path.splitext(os.path.basename(file_name))[0]
    temp_dir = os.path.join(os.path.dirname(file_name), ".temp")

    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    for i in range(start_page - 1, end_page):
        writer = PdfWriter()
        writer.add_page(input_pdf.pages[i])
        output_path = os.path.join(temp_dir, f"{base_name}-page{i + 1}.pdf")

        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)

def merge_pdf(file_name, start_page, end_page):
    merge_pdf = PdfMerger()
    base_name = os.path.splitext(os.path.basename(file_name))[0]
    temp_dir = os.path.join(os.path.dirname(file_name), ".temp")

    for i in range(start_page - 1, end_page):
        input_path = os.path.join(temp_dir, f"{base_name}-page{i + 1}.pdf")
        merge_pdf.append(open(input_path, "rb"))
    
    merged_file_path = os.path.join(os.path.dirname(file_name), f"{base_name}_pages_{start_page}-{end_page}.pdf")

    with open(merged_file_path, "wb") as output_pdf:
        merge_pdf.write(output_pdf)
    
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    
    return merged_file_path

def split_and_merge_pdf(file_name, start_page, end_page):
    split_pdf(file_name, start_page, end_page)
    merged_pdf_path = merge_pdf(file_name, start_page, end_page)
    return merged_pdf_path
