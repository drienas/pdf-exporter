"""
Python Multiexporter for Predefined View

Exportiere Daten aus der benutzerdefinierten Ansicht
im Jobrouter als CSV, XLSX, PDF

by Daniel Rienas, July 2019+
"""
import time
from datetime import datetime


class file_outputter:
    def __init__(self, savedir, hostdata):
        self.savedir = savedir
        self.host = hostdata[0]
        self.port = hostdata[1]

    def generate_new_filename(self, xt):
        fn = self.get_name()
        filename = f"{self.savedir}{fn}.{xt}"
        fileurl = f"{self.host}/files/{fn}.{xt}"
        return filename, fileurl

    def get_name(self):
        return f"{datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S-%f')}"
