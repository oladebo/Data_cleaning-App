# This data cleaning application

"""
Create a python application that can take dataset and clean the dataset :

1. It should ask for dataset path and name.
2. it should check number of duplicates and remove all duplicates 
3. it should check for missing values .
4. if any columns that is numerics, it should replaced it with nulls with mean else it should drop
at the end it should save the data as clean data and also return duplicates records, clean-data
"""

# Import Required dependencies

import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

#data_path = 'sales.xlsx'
#data_name = 'jan_sales.'

def data_cleaning_master(data_path,data_name):

    print("Thank you for given the details !")

    # Checking if path exists
    #sec = random.randint(1, 4)  # generating random numbers

    sec = random.randint(1, 4)

    # Print delay message
    print(f"Please wait for {sec}seconds ! checking file path")
    time.sleep(sec)

    if not os.path.exists(data_path):
        print("Incorrect path try again! Try again with correct path")
        return
    else:
        # Checking the data type or file type
        if data_path.endswith('.csv'):
            print('Dataset is csv !')
            data = pd.read_csv(data_path, encoding_errors='ignore')


        elif data_path.endswith('.xlsx'):
            print('Dataset is excel file !')
            data = pd.read_excel(data_path)

        else:
            print("Uknown file type !")
            return
        
    # Print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec}seconds ! checking for total columns and rows")
    time.sleep(sec)




    # Showing numbers of records
    print(f"Dataset contain total rows: {data.shape[0]} \n Total Columns: {data.shape[1]} ")


    # Start data Cleaning

    # Print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec}seconds ! checking for total duplicates")
    time.sleep(sec)
    

    # Checking duplicate
    duplicates = data.duplicated()
    total_duplicate = data.duplicated().sum

    print(f"Datasets has duplicates record :{total_duplicate}")


    # Print delay message
    sec = random.randint(1, 8)
    print(f"Please wait for {sec}seconds ! Savings for total duplicates rows")
    time.sleep(sec)

    # Saving duplicate
    if total_duplicate()> 0:
        duplicate_records =data[duplicates]
        duplicate_records.to_csv(f"{data_name}_duplicates.csv", index=None)


    # Deleting duplicates
    df = data.drop_duplicates()

    # Print delay message
    sec = random.randint(1, 5)
    print(f"Please wait for {sec}seconds ! checking for missing value records")
    time.sleep(sec)


    # Find the Missing Values
    total_missing_value = df.isnull().sum().sum()
    missing_value_by_columns = df.isnull().sum()

    print(f'Total Dataset has total missing value:{total_missing_value}')
    print(f'Dataset contain missing value by columns \n {missing_value_by_columns}')

    # Dealing with missing values
    # fillna -- int and float
    # dropna -- any object

    # Print delay message
    print(f"Please wait for {sec}seconds ! Cleaning the datasets")
    time.sleep(sec)

    columns = df.columns

    for col in columns:
        if df[col].dtype in (float, int):
            df[col] = df[col].fillna(df[col].mean())

        else:
            # Dropping all rows with missing record of non-numbers in col
            df.dropna(subset= col, inplace = True)

    
    # Print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec}seconds ! Exporting Clean Dataset")
    time.sleep(sec)


    # Dataset is clean
    print(f'Congrat i! Dataset is cleaned n\ Number of Row:{df.shape[0]} Number of Columns:{df.shape[1]}')

    # Saving the clean Dataset

    df.to_csv(f'{data_name}_Cleaned_data.csv', index=None)
    print("Data is Saved !")

if __name__ == "__main__":

    print("Welcome to Data Cleaning Master App")
    # Ask file and path name
    data_path = input("Please enter dataset path_name:")
    data_name = input("Please enter data_name:")

    # Calling the function
    data_cleaning_master(data_path, data_name)
    
    