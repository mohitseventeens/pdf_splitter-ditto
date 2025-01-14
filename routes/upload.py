from flask import Blueprint, request, redirect, url_for, render_template, flash
import os
from werkzeug.utils import secure_filename

upload_bp = Blueprint('upload', __name__)
UPLOAD_FOLDER = 'uploads/'  # Ensure this folder exists
ALLOWED_EXTENSIONS = {'pdf'}

# Ensure the uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'pdfFile' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['pdfFile']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        page_ranges = request.form['pageRanges']
        # Redirect to process file with page ranges
        return redirect(url_for('process.split_pdf', filename=filename, page_ranges=page_ranges))
    else:
        flash('Allowed file types are pdf')
        return redirect(request.url)
