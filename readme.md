
# Surya_OCR

## Overview
This project provides an OCR (Optical Character Recognition) API built using **FastAPI** to process image and PDF files, extracting text content. It also includes utility functions for OCR processing using the **surya** OCR engine. The API allows users to upload individual files or zip archives containing multiple files, and it returns OCR results as text files. This system is designed for easy integration into larger workflows, providing fast and efficient text extraction.

## Features
- **File Upload:** Upload a single image or PDF file for OCR processing.
- **Batch Processing:** Upload a zip file containing multiple images or PDFs, and get OCR results for all files in the zip.
- **OCR Models:** Utilizes the **surya** OCR engine for text detection and recognition from various image formats and PDF documents.
- **Result Output:** OCR results are saved to text files, which can be downloaded individually or in a zip archive containing results for all processed files.
- **Cleanup:** Automatically cleans up temporary directories used during processing to keep the system tidy.

---

## Requirements
To run this project, you need to have the following tools installed:
- **Python 3.10+**
- **Anaconda/Miniconda** (for managing the Conda environment)
- **FastAPI** (for creating the API server)
- **Uvicorn** (for running the FastAPI app)
- **surya** OCR engine (for text recognition)
- **pdf2image** (for converting PDF pages into images)
- **Pillow** (for image processing)
- **zipfile** (for handling zip files)

---

## Setting up the Environment with Conda

### 1. Install Conda
If Conda is not already installed, download and install it from the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/) website.

### 2. Create a Conda Virtual Environment
Run the following commands to set up and activate a Conda virtual environment for the project:

```bash
# Create a new Conda environment
conda create --name surya_ocr python=3.10 -y

# Activate the Conda environment
conda activate surya_ocr
```

### 3. Install Dependencies
With the Conda environment activated, install the required dependencies:

```bash
# Install project dependencies
pip install -r requirements.txt

# Install surya OCR engine
pip install surya-ocr
```

> **Note:** The model weights for the **surya** OCR engine will download automatically the first time you run the application.

If you require GPU support, ensure CUDA is properly installed for PyTorch. Refer to the [PyTorch installation guide](https://pytorch.org/get-started/locally/) for details.

---

## Project Structure
```plaintext
OCR/
├── ocr_api/
│   ├── main.py              # FastAPI server script
│   ├── ocr_utils.py         # Utility functions for OCR processing
│   └── __pycache__/         # Cache files
├── ocr_functions.ipynb      # Jupyter notebook for OCR processing
├── requirements.txt         # Python dependencies for the project
└── README.md                # Project documentation
```

---

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
Accepts a single file (image or PDF) for OCR processing.

#### Request:
- **Content-Type:** `multipart/form-data`
- **Body:** Upload a single image or PDF file.

#### Response:
- **200 OK:** Text file with OCR results.
- **500 Internal Server Error:** Processing error.

Example:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/process_ocr/' -F 'file=@path_to_file.pdf'
```

### 3. `POST /process_folder/`
Accepts a zip file containing multiple images or PDFs and returns a zip of OCR results.

#### Request:
- **Content-Type:** `multipart/form-data`
- **Body:** Upload a zip file containing images or PDFs.

#### Response:
- **200 OK:** Zip file with OCR results.
- **500 Internal Server Error:** Processing error.

Example:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/process_folder/' -F 'zip_file=@path_to_folder.zip'
```

---

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/Meetdhote/Surya_ocr_api.git
```

### 2. Activate the Conda Environment
```bash
conda activate surya_ocr
```

### 3. Run the FastAPI Server
```bash
cd ocr_api
uvicorn ocr_api.main:app --reload
```
This will start the server locally at `http://127.0.0.1:8000`.

### 4. Access the API
- **Root:** `http://127.0.0.1:8000/`
- **Swagger UI (API Docs):** `http://127.0.0.1:8000/docs`
- **ReDoc Docs:** `http://127.0.0.1:8000/redoc`

---

## Additional Notes
- Ensure proper permissions for uploaded files and output directories.
- Temporary files will be automatically cleaned up after processing.

---

## Dependencies
- fastapi
- uvicorn
- surya-ocr
- pdf2image
- Pillow

### Optional (for GPU Support):
- CUDA, TensorFlow, or PyTorch for enhanced OCR processing speed.
