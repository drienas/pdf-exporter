"""
Python Multiexporter for Predefined View

Exportiere Daten aus der benutzerdefinierten Ansicht
im Jobrouter als CSV, XLSX, PDF

by Daniel Rienas, July 2019+
"""
from .dataformat import format_data as fd


def export_to_excel(data, fop):
    data = fd(data)
    fn, url = fop.generate_new_filename('xlsx')
    data.to_excel(fn, index=False)
    return url
