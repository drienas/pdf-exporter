"""
Python Multiexporter for Predefined View

Exportiere Daten aus der benutzerdefinierten Ansicht
im Jobrouter als CSV, XLSX, PDF

by Daniel Rienas, July 2019+
"""
from .dataformat import format_data as fd
import pdfkit as pdf
import os
import time
import random
import datetime

#    width: 640px;
#  color: #333;


def export_to_pdf(data, fop):
    data = fd(data)
    fn, url = fop.generate_new_filename('pdf')

    style = """
    table, h3 {  
   
    font-family: Helvetica, Arial, sans-serif; 

    border-collapse: 
    collapse; border-spacing: 0; 
    }

    td, th { border: 1px solid #CCC; height: 30px; } 

    th {  
        background: #F3F3F3; 
        font-weight: bold; 
    }

    td {  
    
        text-align: center; 
    }
    """

    header_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>PDF Export vom """ + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + """ Uhr</title>
    <style>
    """ + style + """
    </style>
    </head>
    <body>
    <h3>PDF Export vom """ + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + """ Uhr</h3>
    """

    footer_html = """
    </body>
    </html>
    """
    table_html = data.to_html(index=False, na_rep='', justify='center')

    table_html = header_html + table_html + footer_html
    pdf.from_string(table_html, fn, options={'orientation': 'Landscape'})
    return url
