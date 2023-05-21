# NLP-Based-Automatic-Tags-Generation-System-on-a-Web-Application

# Auto Suggest Tags - Proof-of-Concept Web Application

This repository contains the code, documents, and datasets for the Auto Suggest Tags project, which aims to create a web application that auto suggests tags and performs content classification based on user-provided text. The project utilizes machine learning models and web APIs to generate tag suggestions for content on the Repurpost platform.

## Repository Structure

- `/api/`: Contains the code and model required to build and deploy the web API using Flask and Render.com.
    - `/import/model_all.pkl`: Serialized export of the machine learning models used by the web API.
    - `app.py`: Python code implementing the Flask API requests and using the `model_all.pkl` to provide tag suggestions.

- `/datasets/`: Includes the datasets used for training and evaluating the machine learning models.
    - `stackoverflow.csv`: Stack Overflow dataset containing text fields for questions and associated tags.
    - `stackoverflow_final.csv`: Pre-processed version of the Stack Overflow dataset for applying natural language processing algorithms.

- `/documents/`: Contains various documents related to the project.
    - `Repurpose high level solution diagram.pdf`: Solution design and architecture diagram.
    - `Repurpost proposed wireframe.pdf`: Wireframe sketches of the user interface.
    - `Repurpost user flows.pdf`: User flows within the Repurpost platform.
    - `Repurpost Project Reflection Paper.pdf`: Detailed reflection on the project journey.
    - `Repurpost - Project Plan.pdf`: Initial project plan and updates.

- `/notebooks/`: Includes Jupyter notebooks for model design and implementation.
    - `Repurpost_StackOverFlow_Raw_Dataset_Cleanup.ipynb`: Data cleaning and pre-processing notebook.
    - `Repurpost_Multi_Label_Classification_(SVC, SGD, Linear Regression) Model_Building.ipynb`: Model building notebook for multi-label tag classification.
    - `Repurpost_StackoverFlow_CNN.ipynb`: Notebook for implementing a CNN model for tag suggestions.
    - `Repurpost_StackOverflow_BERTModel.ipynb`: Notebook for implementing a BERT model for tag prediction.
    - `Repurpost_StackOverflow_LSTM_RNNModel.ipynb`: Notebook for implementing an LSTM RNN model for tag prediction.

## Web API - Render.com

Render.com is a unified cloud platform used to create, build, and deploy apps, web APIs, and websites.

### API Contracts

#### Auto Suggest Tags

The API provides the functionality to suggest and create tags based on user-provided content.

**End Points:**

- `/tagSuggestsAPI`: Endpoint for tag suggestions.

**API Input:**

- `content` (string): The text data from the content description. The maximum length of the content is not currently restricted.

Example:

**API Output:**

- List of strings: The output contains a list of tags predicted by the machine learning model. The list may be empty or contain one or more tags.

Example:

## Web Interface - Retool.com

Retool.com is a low-code platform that allows rapid and easy creation of internal tools. It provides building blocks for creating web interfaces and supports integration with web APIs and databases.

### Home App

The home app includes a dashboard and a create section similar to Repurpost's home page. The create section navigates to the Content Creation App.

### Content Creation App

The Content Creation App is the main page where users provide textual content for their posts.
This project is licensed under the Apache License 2.0. For more information, please refer to the `LICENSE` file included in this repository.

For any inquiries or questions, please contact yashwanthbalan75@gmail.com.
