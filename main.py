from flask import Flask, render_template, request
import pandas as pd
from cme_detector import detect_cme
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('index.html', message="Upload a CSV file to detect CME.")

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', message="No file uploaded.")

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', message="No file selected.")

    try:
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Read the uploaded file
        df = pd.read_csv(filepath)
        message, warning = detect_cme(df)

        return render_template(
            'result.html',
            message=message,
            warning=warning,
            filename=file.filename
        )

    except Exception as e:
        return render_template('index.html', message=f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)
