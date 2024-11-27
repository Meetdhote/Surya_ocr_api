import os
from PIL import Image
from surya.ocr import run_ocr
from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor
from pdf2image import convert_from_path

# Helper function to process input (image or PDF)
def process_input(file_path):
    # Check the file extension to handle different types of files
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        return [Image.open(file_path)]  # For images, return as list with one image
    elif file_path.lower().endswith('.pdf'):
        pages = convert_from_path(file_path, 300)  # For PDFs, convert to images
        return pages
    else:
        raise ValueError("Unsupported file type. Please provide a valid image or PDF file.")

# Function to save OCR output to a text file
def save_ocr_output(file_path, ocr_result, output_folder):
    # Generate the output file name by removing the extension
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_text_file = os.path.join(output_folder, f"{base_name}.txt")
    with open(output_text_file, 'w') as file:
        file.write(ocr_result)  # Save OCR result to the text file
    return output_text_file  # Return the path of the saved output file

# Function to run OCR on a given file (image or PDF)
def run_ocr_on_file(file_path, output_folder):
    # Process the input file (image or PDF)
    images = process_input(file_path)
    langs = ["en"]  # Languages to be used for OCR

    # Load the detection and recognition models
    det_processor, det_model = load_det_processor(), load_det_model()
    rec_model, rec_processor = load_rec_model(), load_rec_processor()

    # Run OCR on the processed images
    predictions = run_ocr(images, [langs] * len(images), det_model, det_processor, rec_model, rec_processor)

    # Extract the text from OCR predictions
    full_text = ""
    for prediction in predictions:
        for text_line in prediction.text_lines:
            full_text += text_line.text + "\n"

    # Save the OCR output to a text file
    return save_ocr_output(file_path, full_text, output_folder)
