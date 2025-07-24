from fpdf import FPDF
import tempfile
import os

def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in text.split('\n'):
        pdf.cell(0, 10, txt=line, ln=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf.output(tmp_file.name)
        tmp_path = tmp_file.name

    with open(tmp_path, "rb") as f:
        pdf_data = f.read()

    os.remove(tmp_path)  # clean up temp file

    return pdf_data  # ✅ Return PDF as bytes
