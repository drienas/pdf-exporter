"""
Python Multiexporter for Predefined View

Exportiere Daten aus der benutzerdefinierten Ansicht
im Jobrouter als CSV, XLSX, PDF

by Daniel Rienas, July 2019+
"""
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Import my Own Libraries
from xformats import format_data as fd, to_csv, to_excel, to_pdf, to_mexcel, file_outputter

# Import ConfigFile
from config import *


# Create New File Outputter
fop = file_outputter(EXPORT_FILE_SAVE_DIR, (LOCALHOST, PORT))

app = Flask(__name__)
CORS(app)


@app.route('/csv', methods=['POST'])
def csv():
    url = to_csv(request.json, fop)
    return jsonify({'success': True, 'uri': url})


@app.route('/xlsx', methods=['POST'])
def xlsx():
    url = to_excel(request.json, fop)
    return jsonify({'success': True, 'uri': url})


@app.route('/pdf', methods=['POST'])
def pdf():
    url = to_pdf(request.json, fop)
    return jsonify({'success': True, 'uri': url})

@app.route('/mxlsx', methods=['POST'])
def mxlsx():
    url = to_mexcel(request.json, fop)
    return jsonify({'success': True, 'uri': url})


@app.route('/files/<path:filename>')
def get(filename):
    return send_from_directory(EXPORT_FILE_SAVE_DIR, filename)


if __name__ == '__main__':
    app.run(host=HOST,
            port=PORT,
            debug=DEBUGMODE)
