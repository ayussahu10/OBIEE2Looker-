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


## Text Generation for Dashboard File Documentation

### Overview
The Text Generation module in the BI Modernisation app creates dashboard files using a pre-trained text generation model. It parses input data, extracts relevant information, and generates YAML-formatted text representing dashboard file structures.

### Libraries Used
- **vertexai**: Library for working with machine learning models and infrastructure.
- **streamlit**: Python library for building interactive web applications.
- **bs4 (Beautiful Soup)**: Library for parsing HTML and XML documents.
- **xml.etree.ElementTree**: Library for parsing XML documents.
- **lxml.etree**: High-performance XML processing library.

### Functionality
- **generate_dashboard_file(Bs_data, r, c, w, h)**:
  - Generates a dashboard file based on input BeautifulSoup data (Bs_data) and layout parameters (r, c, w, h).
  - Extracts title, model, chart type, and fields from the input data.
  - Uses a text generation model to create YAML-formatted text representing the dashboard file structure.
  - Displays the generated text to the user and saves it locally.

### Input Parameters
- **Bs_data**: BeautifulSoup object containing parsed XML data.
- **r, c, w, h**: Layout parameters (row, column, width, height) for positioning dashboard elements.

### Output
- Generates YAML-formatted text representing dashboard file structures.
- Displays the text to the user and saves it locally.

### Usage
1. Ensure required libraries are installed.
2. Initialize the Vertex AI text generation model.
3. Call the `generate_dashboard_file()` function with appropriate parameters to generate dashboard files.

### Notes
- Ensure proper input data formatting for accurate information extraction.
- Verify the generated YAML text to ensure it matches the desired dashboard file structure.


## Text Generation for Model File Documentation

### Overview
The Text Generation module in the BI Modernisation app creates model files using a pre-trained text generation model. It takes a DataFrame as input, generates YAML-formatted text based on the provided data, and displays the generated content to the user.

### Libraries Used
- **vertexai**: Library for working with machine learning models and infrastructure.
- **streamlit**: Python library for building interactive web applications.

### Model Initialization
- The Vertex AI text generation model is initialized with specific parameters for temperature, max output tokens, top p, and top k.

### Functionality
- **generate_model_file(df)**:
  - Generates a model file based on the input DataFrame (df).
  - Creates a prompt for the model containing the DataFrame data and specific instructions.
  - Feeds the prompt to the text generation model to generate YAML-formatted text representing the model file structure.
  - Displays the generated text to the user and saves it locally on the device.

### Input Parameters
- **df**: Pandas DataFrame containing the data to be used in the model file.

### Output
- Generates YAML-formatted text representing the structure and content of the model file.
- Displays the text to the user and saves it locally on the device.

### Usage
1. Ensure the required libraries are installed.
2. Initialize the Vertex AI text generation model.
3. Call the `generate_model_file()` function with the appropriate DataFrame parameter to generate model files based on input data.

### Notes
- Verify the generated YAML text to ensure it matches the desired model file structure.
- Optionally, upload the generated file to GitHub using the provided `commit_and_push_to_github()` function (commented out in the code).



