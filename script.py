from os.path import isfile
import eel    
import pandas as pd
import os
import json
from pandas import Timestamp
import numpy as np

eel.init('web')

def clean_and_convert_to_json(data):
    # Extract the data for key 1227 and ensure all data types are JSON serializable
    cleaned_data = {}
    for key, value in data.items():
        item = value[1227]

        # Convert Timestamp to string format
        if isinstance(item, pd.Timestamp):
            cleaned_data[key] = item.strftime('%Y-%m-%d')

        # Convert NaN to None (or an empty string, if that's more appropriate for your frontend)
        elif pd.isna(item):
            cleaned_data[key] = None

        # For all other data types, use them as they are
        else:
            cleaned_data[key] = item

    return cleaned_data

@eel.expose
def add_one(x: int) -> int:
    return x + 1

@eel.expose
def find_book(nit_code):
    df_original = pd.read_excel("book-database.xlsm", sheet_name="Book Master DB")
    row_result = df_original[df_original['NIT_Code'] == nit_code]
    rowDict = row_result.to_dict()

    
    clean_data = clean_and_convert_to_json(rowDict)
    print(clean_data)
    return clean_data 

    
eel.start('index.html')
