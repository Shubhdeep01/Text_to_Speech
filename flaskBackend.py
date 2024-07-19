import os
import tempfile
from flask import Flask, request, jsonify
import fitz  # PyMuPDF
from flask_cors import CORS
import pyttsx3
import pythoncom

app = Flask(__name__)
CORS(app)

# Initialize COM for pyttsx3 if not already initialized
if not pyttsx3.init().__dict__.get('CoInitialize'):
    pythoncom.CoInitialize()

# Define the base directory for audio files
base_dir = r"D:\python (harry)\mini prj\Audio"

def generate_audio(text, language, filename):
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        # Set voice based on language
        for voice in voices:
            if language in voice.languages:
                engine.setProperty('voice', voice.id)
                break
        
        output_path = os.path.join(base_dir, filename)
        
        engine.save_to_file(text, output_path)
        engine.runAndWait()
        return output_path
    
    except Exception as e:
        print(f"Error in text-to-speech generation: {e}")
        return None

def extract_pdf_text(pdf_path):
    try:
        pdf_content = ""
        pdf_document = fitz.open(pdf_path)
        
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            pdf_content += page.get_text()
        
        return pdf_content.strip()
    
    except Exception as e:
        print(f"Error extracting PDF content: {e}")
        return None

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    try:
        print("Endpoint '/upload_pdf' called")
        
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        pdf_file = request.files['file']
        if pdf_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if not pdf_file.filename.lower().endswith('.pdf'):
            return jsonify({'error': 'File is not a PDF'}), 400
        
        # Save uploaded PDF file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
            pdf_file.save(temp_pdf.name)
            pdf_content = extract_pdf_text(temp_pdf.name)
        
        if pdf_content is None:
            return jsonify({'error': 'Failed to extract PDF content'}), 500
        
        print(f"PDF content extracted: {pdf_content}")
        
        # Generate audio from PDF content (assuming language is 'en' for example)
        output_filename = 'output.mp3'  # You can generate a unique filename here if needed
        output_path = generate_audio(pdf_content, 'en', output_filename)
        
        if output_path:
            return jsonify({'message': 'Text-to-speech conversion successful', 'output_path': output_filename, 'pdf_text': pdf_content}), 200
        else:
            return jsonify({'error': 'Text-to-speech conversion failed'}), 500
    
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(port=5000)
