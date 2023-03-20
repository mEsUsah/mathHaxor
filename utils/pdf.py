import pdfkit

def create(html,css, file_name):
    return pdfkit.from_string(html, file_name,css=css)