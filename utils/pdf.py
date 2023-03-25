import pdfkit
import tkinter.filedialog as filedialog

def create(html,css, file_name):
    return pdfkit.from_string(html, file_name,css=css)

def guiSaveAsPath():
    return filedialog.asksaveasfilename(
            filetypes=(("PDF", "*.pdf"), ("All files", "*.*")),
            defaultextension=".pdf")