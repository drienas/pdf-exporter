"""
Python Multiexporter for Predefined View

Exportiere Daten aus der benutzerdefinierten Ansicht
im Jobrouter als CSV, XLSX, PDF

by Daniel Rienas, July 2019+
"""
import pandas as pd
import time
import datetime
from .dataformat import format_data as fd


def export_to_mexcel(data, fop):
    rdata = data

    fn, url = fop.generate_new_filename('xlsx')
    writer = pd.ExcelWriter(fn, engine='xlsxwriter')

    for d in data:
        xdata = {
            "rows": d['rawData'],
            "keep": d['keep'],
            "cols": d['columnNames']
        }
        ndata = fd(xdata)
        ndata.to_excel(writer, sheet_name=d['title'],
                  index=False, startrow=2, header=False)
        workbook = writer.book
        worksheet = writer.sheets[d['title']]
        worksheet.set_landscape()
        worksheet.set_paper('A4')
        title_format = workbook.add_format({
            'bold': True})
        worksheet.write(0, 0, datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S'), title_format)
        if 'title' in d:
            worksheet.write(0, 1, d['title'], title_format)

        header_format = workbook.add_format({
            'bold': True,
            'rotation': 45,
            'valign': 'bot',
            'align': 'center',
            'border': 1})

        for col_num, value in enumerate(ndata.columns.values):
            worksheet.write(1, col_num, value, header_format)


    writer.save()
    return url
