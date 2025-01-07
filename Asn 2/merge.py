import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_folder, output_folder, output_filename):
    # Create a PdfMerger object
    merger = PdfMerger()

    # Iterate through all the PDF files in the input folder
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith('.pdf'):
            file_path = os.path.join(input_folder, filename)
            merger.append(file_path)

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Save the merged PDF to the specified output folder
    output_path = os.path.join(output_folder, output_filename)
    merger.write(output_path)
    merger.close()

    print(f'Merged PDF saved as {output_path}')

# Example usage
input_folder = r'D:\7 sem\GAN\Assignment 2\New folder (2)'
output_folder = r'D:\7 sem\GAN\Assignment 2\New folder (2)'
output_filename = 'merged_document.pdf'

merge_pdfs(input_folder, output_folder, output_filename)
