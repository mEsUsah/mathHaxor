import pdfkit

def create(html, file_name):
    return pdfkit.from_string(html, file_name)