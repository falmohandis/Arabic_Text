import numpy as np
import pandas as pd
import os

# In case you need to install the pdf2image package, uncomment the line below:
# !pip install pdf2image
import pdf2image
from pdf2image import convert_from_path

# Iterate through the pdf files obtained from the pdf_loader function, convert them into images and then save the images into a folder a folder called page_images


def pdf_to_images(input_folder, output_folder):
    """
    Converts all PDF files in 'input_folder' to images and saves them into 'page_images'.
    
    Each image file is named using the original PDF filename and the page number.
    """
    
    # Make sure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Create a list of all PDF files in the input folder
    try:
        pdf_files = [
            os.path.join(input_folder, f)
            for f in os.listdir(input_folder)
            if f.lower().endswith('.pdf') and os.path.isfile(os.path.join(input_folder, f))
        ]
    except ValueError as e:
        # This part runs if there are no PDF files in the input folder
        print(f"No PDF files found in {input_folder}. Please check the folder path.")
        print(e)
        raise  # Re-raises the same exception, stopping the program

    
    for pdf_file in pdf_files: 
        # Convert each PDF file to images one by one
        images = convert_from_path(pdf_file)

        # Extract the PDF filename without its directory path and file extension (*.pdf).
        pdf_name = os.path.splitext(os.path.basename(pdf_file))[0]
        

        # Iterate over the images returned for each page in the PDF.
        # 'enumerate' provides both the page index (i) and the image object.
        for i, image in enumerate(images):

            # Construct a filename for the image that includes the original PDF name and the page number.
            image_filename = f"{pdf_name}_page_{i + 1}.jpg"

            # Save the image as a JPEG in the output folder.
            image.save(os.path.join(output_folder, image_filename),             # os.path.join ensures a proper file path regardless of operating system.
                        "JPEG",           # The "JPEG" argument specifies the format.
                        quality=95,       # Highest quality without hitting extreme sizes
                        optimize=True,    # Reduces file size intelligently
                        progressive=True  # Enables progressive JPEG (loads gradually)
                    )
    
    print(f"Converted {len(pdf_files)} PDF files into images and saved them to {output_folder}.")



# Start from Current Directory:
current_directory = os.getcwd()

# Define the path to the input_pdfs folder
input_pdfs_path = os.path.join(current_directory, 'input_pdfs')

# images_folder= os.path.join(current_directory, 'page_images')
output_images_path = os.path.join(current_directory, 'page_images')


# Run the pdf_to_images function
pdf_to_images(input_pdfs_path, output_images_path)