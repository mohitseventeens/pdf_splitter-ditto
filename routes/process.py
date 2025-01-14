from flask import Blueprint, request, render_template, current_app
import os
from PyPDF2 import PdfReader, PdfWriter

process_bp = Blueprint('process', __name__)
UPLOAD_FOLDER = 'uploads/'

@process_bp.route('/process', methods=['GET'])
def split_pdf():
    filename = request.args.get('filename')
    page_ranges = request.args.get('page_ranges')
    if not filename or not page_ranges:
        return "Invalid request", 400

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    try:
        reader = PdfReader(file_path)
        sections = page_ranges.split(',')
        output_files = []
        for index, section in enumerate(sections):
            start, end = map(int, section.split('-'))
            writer = PdfWriter()
            for page in range(start-1, end):  # Pages are 0-indexed
                writer.add_page(reader.pages[page])
            
            output_filename = f'extracted_section_{index+1}.pdf'
            output_path = os.path.join(current_app.static_folder, output_filename)
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            output_files.append(output_filename)

        return render_template('result.html', files=output_files)
    except Exception as e:
        return str(e), 500
