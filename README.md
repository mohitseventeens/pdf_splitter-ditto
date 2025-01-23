# Flask PDF Splitter

This is a simple Flask application that allows users to split PDF files into sections based on specified page ranges.
Built using `ditto`. Learn more about `ditto` here: [https://github.com/yoheinakajima/ditto](https://github.com/yoheinakajima/ditto).

## Features

- Upload a PDF file.
- Define custom page ranges to split the PDF into multiple sections.
- Download the resulting PDF sections.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mohitseventeens/pdf_splitter-dittoflask.git
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

7. Run the application:

   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000` by default.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
