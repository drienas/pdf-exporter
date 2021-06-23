"""
Python Multiexporter for Predefined View

Exportiere Daten aus der benutzerdefinierten Ansicht
im Jobrouter als CSV, XLSX, PDF

by Daniel Rienas, July 2019+
"""
import pdfkit as pdf


def export_html_to_pdf(data, fop):

    fn, url = fop.generate_new_filename('pdf')
    html = data['html']

    options = {}
    if 'options' in data:
        options = data['options']

    # options={
    #     'orientation': 'Landscape',
    #     'page-size': 'A3'
    # }

    pdf.from_string(html, fn, options)
    return url
