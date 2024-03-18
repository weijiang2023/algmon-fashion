from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert each page of the PDF to an image
    pages = convert_from_path(pdf_path)

    # Save each page as an image file
    for i, page in enumerate(pages):
        image_path = os.path.join(output_folder, f"page_{i+1}.jpg")  # Change jpg to your preferred image format
        page.save(image_path, 'PNG')  # Change JPEG to the format you prefer

if __name__ == "__main__":
    pdf_path = "../show.covers.reviews.pdf"  # Path to your PDF file
    output_folder = "covers"  # Folder to save the images

    pdf_to_images(pdf_path, output_folder)
