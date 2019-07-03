"""
Python Multiexporter for Predefined View

Exportiere Daten aus der benutzerdefinierten Ansicht
im Jobrouter als CSV, XLSX, PDF

by Daniel Rienas, July 2019+
"""
import pandas as pd


def format_data(data):
    df = pd.DataFrame(data["rows"])
    df = df[data['keep']]
    df.rename(columns=data['cols'], inplace=True)
    return df
