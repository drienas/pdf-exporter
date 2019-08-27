"""
Python Multiexporter for Predefined View

Exportiere Daten aus der benutzerdefinierten Ansicht
im Jobrouter als CSV, XLSX, PDF

by Daniel Rienas, July 2019+
"""
import pandas as pd
import numpy as np


def format_data(data):
    df = pd.DataFrame(data["rows"])
    df = df[data['keep']]
    df.rename(columns=data['cols'], inplace=True)
    df.replace([None], np.nan, inplace=True)
    # df.replace(False, 'Nein', inplace=True)
    # df.replace(True, 'Ja', inplace=True)
    print(df.head())
    booleandf = df.select_dtypes(include=[bool])
    booleanDictionary = {True: 'Ja', False: 'Nein'}
    for column in booleandf:
        df[column] = df[column].map(booleanDictionary)
    # df.replace({True:'Ja',False:'Nein'}, inplace=True)
    print(df.head())
    return df
