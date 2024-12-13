# Verba Vision Pro

## Project Overview
Verba Vision Pro is an advanced digital solution for efficient and accurate document and spreadsheet management. This project integrates Optical Character Recognition (OCR) technology and automated spell-checking to enhance productivity and minimize errors in document handling. The platform features a robust backend built with Flask and an intuitive frontend using HTML, CSS, and JavaScript.

## Features
1. **Text Extraction and OCR Technology**
   - Extracts text from scanned images, PDFs, and other document formats.
   - Uses advanced OCR for accurate text recognition.

2. **Automated Spell Checking**
   - Automatically detects and corrects spelling errors in Excel spreadsheets.
   - Provides correction suggestions with options for manual or automatic fixes.

3. **Data Security**
   - Ensures secure handling of sensitive data with encryption and role-based access control.

4. **User-Friendly Interface**
   - Responsive and intuitive UI with easy navigation.
   - Real-time feedback for document uploads and processing.

5. **Integration and Scalability**
   - Unified platform for OCR and spell-checking.
   - Built to handle large datasets and scalable for future enhancements.

## Technologies Used
- **Backend:** Flask, Python
- **Frontend:** HTML5, CSS3, JavaScript
- **OCR Engine:** Tesseract, Google Vision API
- **Spell Checking:** PySpellChecker, Microsoft Word API
- **Security:** SSL/TLS, AES Encryption

## System Architecture
### Workflow
1. **Input Sources**
   - Accepts PDF, JPEG, and Excel files for processing.
2. **Image Processing**
   - Separates and analyzes document layouts.
3. **OCR Integration**
   - Converts scanned images into editable text.
4. **Spell Checking**
   - Detects and corrects spelling errors.
5. **Output**
   - Provides corrected text and highlighted changes.

## Modules
### 1. Text Extraction and OCR
   - Preprocessing: Noise reduction, deskewing.
   - Post-processing: Formatting and artifact removal.

### 2. Automated Spell Checking
   - Text parsing and error detection.
   - Suggestions for corrections and batch processing.

### 3. Data Security and Confidentiality
   - Encryption for data in transit and at rest.
   - Multi-factor authentication and access logging.

### 4. User Interface
   - File upload with drag-and-drop support.
   - Progress bars and real-time notifications.

## Installation
### Prerequisites
- Python 3.10 or later
- Flask
- Tesseract OCR

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/verba-vision-pro.git
   ```
2. Navigate to the project directory:
   ```bash
   cd verba-vision-pro
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Access the application at `http://localhost:5000`.

## Usage
1. Upload documents or images.
2. View extracted text and spell-check results.
3. Download corrected files.

## Future Enhancements
1. Multilingual OCR and spell-checking.
2. Integration with cloud storage platforms (e.g., Google Drive, Dropbox).
3. Advanced spell-checking using machine learning.
4. Mobile app for on-the-go document processing.

---

Developed by: Mithun M S (212222240067) and Sandhya B N

