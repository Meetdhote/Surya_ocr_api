
# Surya OCR 

## Overview
This project provides an OCR (Optical Character Recognition) API built using **FastAPI** to process image and PDF files, extracting text content. It also includes utility functions for OCR processing using the **surya** OCR engine. The API allows users to upload individual files or zip archives containing multiple files, and it returns OCR results as text files. This system is designed for easy integration into larger workflows, providing fast and efficient text extraction.

## Features
- **File Upload:** Upload a single image or PDF file for OCR processing.
- **Batch Processing:** Upload a zip file containing multiple images or PDFs, and get OCR results for all files in the zip.
- **OCR Models:** Utilizes the **surya** OCR engine for text detection and recognition from various image formats and PDF documents.
- **Result Output:** OCR results are saved to text files, which can be downloaded individually or in a zip archive containing results for all processed files.
- **Cleanup:** Automatically cleans up temporary directories used during processing to keep the system tidy.

## Requirements
To run this project, you need to have the following tools installed:
- **Python 3.10+**
- **FastAPI** (for creating the API server)
- **Uvicorn** (for running the FastAPI app)
- **surya** OCR engine (for text recognition)
- **pdf2image** (for converting PDF pages into images)
- **Pillow** (for image processing)
- **zipfile** (for handling zip files)

### Installation
You need Python 3.10+ and **PyTorch** to use this project. If you are not using a Mac or a GPU machine, you may need to install the CPU version of **torch** first. Refer to the [PyTorch installation guide](https://pytorch.org/get-started/locally/) for specific instructions.

To install all dependencies, including **surya OCR**, follow these steps:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install the **surya** OCR engine:
   ```bash
   pip install surya-ocr
   ```
   The model weights will automatically download the first time you run **surya**.

If you need GPU support, ensure CUDA is properly installed for PyTorch.

### Dependencies
- fastapi
- uvicorn
- surya-ocr
- pdf2image
- Pillow

### Optional (for running with GPU support):
- CUDA, TensorFlow, or PyTorch for enhanced OCR processing speed with GPU.

## Project Structure
OCR/
├── ocr_api/
│   ├── main.py              # FastAPI server script
│   ├── ocr_utils.py         # Utility functions for OCR processing
│   └── __pycache__/         # Cache files
├── ocr_functions.ipynb      # Jupyter notebook for OCR processing
├── requirements.txt         # Python dependencies for the project
└── README.md                # Project documentation
```

## Endpoints

### 1. `GET /`
The root endpoint returns a welcome message indicating the API is running.

#### Response:
```json
{
  "message": "Welcome to the OCR API!"
}
```

### 2. `POST /process_ocr/`
This endpoint accepts a single file (image or PDF) for OCR processing.

#### Request:
- **Content-Type:** `multipart/form-data`
- **Body:** Upload a single image or PDF file (PDF, PNG, JPG, JPEG, BMP, TIFF).

#### Response:
- **200 OK:** A text file containing the OCR results for the uploaded file.
- **500 Internal Server Error:** If the file processing fails for any reason.

Example:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/process_ocr/' -F 'file=@path_to_file.pdf'
```

### 3. `POST /process_folder/`
This endpoint accepts a zip file containing multiple images or PDFs, processes each file inside, and returns a zip of the OCR results for all processed files.

#### Request:
- **Content-Type:** `multipart/form-data`
- **Body:** Upload a zip file containing images or PDFs.

#### Response:
- **200 OK:** A zip file containing text files for each processed file inside the zip.
- **500 Internal Server Error:** If any errors occur during the batch processing.

Example:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/process_folder/' -F 'zip_file=@path_to_folder.zip'
```

## OCR Utility Functions

### `ocr_utils.py`
The utility functions in `ocr_utils.py` are responsible for the following tasks:
- **Image/PDF Handling:** Convert PDFs to images or process image files directly.
- **OCR Processing:** Perform OCR on the images using the surya OCR engine.
- **Output Handling:** Save the OCR results to text files.

Key functions:
1. **`process_input(file_path)`**: Processes the uploaded file (image or PDF). For images, it returns the image object; for PDFs, it converts the pages to images.
2. **`run_ocr_on_file(file_path, output_folder)`**: Runs OCR on a single file (image or PDF) and saves the extracted text.
3. **`save_ocr_output(file_path, ocr_result, output_folder)`**: Saves the OCR result to a text file in the output folder.

## How to Run

### 1. Clone the repository:
```bash
git clone https://github.com/Meetdhote/Surya_ocr_api.git
cd OCR/ocr_api
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
pip install surya-ocr
```

### 3. Run the FastAPI server:
```bash
uvicorn main:app --reload
```
This will start the server locally at `http://127.0.0.1:8000`.

### 4. Access the API:
Open your browser and go to:
- **Root:** `http://127.0.0.1:8000/` (Welcome message)
- **Swagger UI (API Docs):** `http://127.0.0.1:8000/docs` (Interactive API documentation)
- **ReDoc Docs:** `http://127.0.0.1:8000/redoc` (Alternative API documentation)


