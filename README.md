# Text-to-Speech Web Application

## Description
This project is a Text-to-Speech (TTS) web application built using Python's Flask framework for the backend and HTML, CSS, and JavaScript for the frontend. It allows users to input text via a web interface, and the backend converts the text into audio using a text-to-speech library (such as `pyttsx3`). The generated speech is then played through the browser.

## Features
- Simple and user-friendly web interface
- Real-time text-to-speech conversion
- Supports multiple voices and speech rates
- Audio playback within the web application

## Technologies Used
### Backend
- Python
- Flask
- pyttsx3 (Text-to-Speech library)

### Frontend
- HTML
- CSS
- JavaScript

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python (3.x recommended)
- pip (Python package manager)

### Steps to Run the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/text-to-speech.git
   cd text-to-speech
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```sh
   python app.py
   ```

5. Open your web browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Enter the desired text in the input field.
2. Click the "Convert to Speech" button.
3. The system will generate and play the speech audio.
4. Optionally, users can modify the voice or speech rate settings.

## Project Structure
```
text-to-speech/
│-- static/
│   ├── styles.css
│   ├── script.js
│-- templates/
│   ├── index.html
│-- app.py
│-- requirements.txt
│-- README.md
```

## Dependencies
- Flask
- pyttsx3

To install all dependencies, run:
```sh
pip install -r requirements.txt
```

## Contributing
If you want to contribute to this project, follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch.
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Flask documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- pyttsx3 documentation: [https://pyttsx3.readthedocs.io/](https://pyttsx3.readthedocs.io/)

