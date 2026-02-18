# Fake-social-media-ID-Detector
Fake Social Media ID Detector is a web-based Machine Learning project that identifies fake social media accounts in real time by analyzing profile and behavioral features such as account age, follower ratio, and activity patterns. Designed to help prevent online fraud and impersonation.
# Fake Social Media ID Detector

## Overview
This project is a simple web application that detects whether a given social media username is likely to be fake or real. It includes a backend built with Flask and a frontend using HTML, CSS, and JavaScript.

## How It Works
- The user enters a social media username in the input box on the webpage.
- The frontend sends this username to the backend API `/detect` using a POST request.
- The backend runs a simple heuristic-based detection logic to classify the username as "Fake" or "Real".
- The detection logic considers the following rules:
  - Usernames that are too short (<3) or too long (>30) are considered fake.
  - Usernames consisting only of digits are considered fake.
  - Usernames containing special characters (e.g., !@#$%) are considered fake.
  - Otherwise, the username is considered real.
- The result is sent back to the frontend and displayed to the user in real-time.

## Project Structure
- `app.py` - Flask backend application serving the frontend and detection API
- `templates/index.html` - Frontend HTML template
- `static/style.css` - Styling for the frontend
- `static/script.js` - Frontend JavaScript for interactions and API calls

## Running the Project Locally
### Prerequisites
- Python 3.x installed
- `pip` package manager

### Installation steps
1. (Optional but recommended) Create a virtual environment:
   ```
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
3. Install Flask:
   ```
   pip install Flask
   ```
4. Run the Flask app:
   ```
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Deployment
For deployment, you can use platforms such as Heroku, AWS Elastic Beanstalk, or any VPS supporting Python/Flask applications. The main points are:
- Ensure you set `app.run()` with appropriate host and port (e.g., `host='0.0.0.0'`)
- Manage dependencies using `requirements.txt` (not included here but can be generated with `pip freeze > requirements.txt`)
- Configure a production-ready web server (e.g., Gunicorn) to serve the app.

## Notes
This project uses a simple heuristic detection approach for demonstration purposes only and is not intended for production use. Real social media ID authenticity requires advanced checks involving online API verifications and machine learning.
