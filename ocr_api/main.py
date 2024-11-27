from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import os
import shutil
import zipfile
from pathlib import Path
from ocr_utils import run_ocr_on_file  # Import the OCR processing function

# Initialize FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
async def read_root():
    # Returns a welcome message when accessing the root URL
    return {"message": "Welcome to the OCR API!"}

# Endpoint for file upload and OCR processing
@app.post("/process_ocr/")
async def process_ocr(file: UploadFile = File(...)):
    # Temporary folder to store the uploaded file
    temp_folder = "/tmp/ocr_input"
    os.makedirs(temp_folder, exist_ok=True)
    
    # Save the uploaded file to the temporary folder
    file_location = os.path.join(temp_folder, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    try:
        # Output folder where OCR results will be saved
        output_folder = "/tmp/ocr_output"
        os.makedirs(output_folder, exist_ok=True)

        # Run OCR processing on the uploaded file and get the result
        result_file = run_ocr_on_file(file_location, output_folder)

        # Return the OCR result file as a downloadable response
        return FileResponse(result_file, media_type='application/octet-stream', filename=os.path.basename(result_file))
    
    except Exception as e:
        # Handle any errors during processing
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Cleanup temporary folder after processing
        shutil.rmtree(temp_folder)

# Endpoint to process a folder of files (via zip upload) and provide download link
@app.post("/process_folder/")
async def process_folder(zip_file: UploadFile = File(...)):
    # Temporary folder to store the uploaded zip file
    temp_folder = "/tmp/ocr_folder_input"
    os.makedirs(temp_folder, exist_ok=True)
    
    # Save the uploaded zip file to the temporary folder
    zip_file_location = os.path.join(temp_folder, zip_file.filename)
    with open(zip_file_location, "wb") as f:
        f.write(await zip_file.read())

    # Folder where the OCR output will be saved
    output_folder = "/tmp/ocr_output"
    os.makedirs(output_folder, exist_ok=True)

    try:
        # Extract the contents of the uploaded zip file
        extracted_folder = os.path.join(temp_folder, "extracted")
        os.makedirs(extracted_folder, exist_ok=True)
        
        with zipfile.ZipFile(zip_file_location, 'r') as zip_ref:
            zip_ref.extractall(extracted_folder)
        
        # Process each file in the extracted folder
        for root, dirs, files in os.walk(extracted_folder):
            for file in files:
                file_path = os.path.join(root, file)
                # Only process image or PDF files
                if file.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                    try:
                        run_ocr_on_file(file_path, output_folder)
                    except Exception as e:
                        # Handle errors if any file fails to process
                        raise HTTPException(status_code=500, detail=f"Error processing file {file}: {str(e)}")

        # Create a zip file of the OCR output folder
        output_zip_path = "/tmp/ocr_output.zip"
        shutil.make_archive(output_zip_path.replace(".zip", ""), 'zip', output_folder)
        
        # Return the zip file as a downloadable response
        return FileResponse(output_zip_path, media_type='application/zip', filename="ocr_output.zip")
    
    except Exception as e:
        # Handle errors during the entire process
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        # Cleanup temporary folder after processing
        shutil.rmtree(temp_folder)
