# BI Modernisation App

## Overview
The BI Modernisation app is designed to facilitate various tasks related to modernizing Business Intelligence (BI) systems. It allows users to select different options and perform actions such as uploading CSV and XML files, generating view, model, and dashboard files based on the uploaded data.

## Structure
- **app.py**: Main script containing the Streamlit application.
- **style.css**: Custom CSS styling for the application.
- **viewFile.py**: Module for generating view files.
- **modelFile.py**: Module for generating model files.
- **dashboardFile.py**: Module for generating dashboard files.

## Libraries Used
- **Streamlit**: A Python library for building interactive web applications.
- **Pandas**: A powerful data manipulation library.
- **Beautiful Soup (bs4)**: A library for pulling data out of HTML and XML files.

## Usage
1. Run `app.py` using a Python interpreter.
2. Access the Streamlit web application in a browser.
3. Select options, upload files, and perform actions as needed.

## Functionality
- **Option Selection**: Users can select two options from dropdown menus.
- **File Upload**: Users can upload a CSV file and one or more XML files. Uploaded files are displayed with details.
- **Action Buttons**:
   - **Generate View File**: Generates a view file based on the uploaded CSV data.
   - **Generate Model File**: Generates a model file based on the uploaded CSV data.
   - **Generate Dashboard File**: Generates dashboard files based on the uploaded XML data.
- **File Generation**: Utilizes specific functions to generate view, model, and dashboard files.
- **Error Handling**: Displays error messages if no file is uploaded or if the wrong file type is selected.

## Notes
- Ensure correct file types are uploaded for each action.
- Provide filenames for model files before downloading.
