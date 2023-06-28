# Code Review and JD Analyzer App

This application provides two main features:
1. **Code Review**: Analyze and review your code snippets.
2. **JD Analyzer**: Analyze and provide insights about Job Descriptions.

Built with Python and Streamlit, the application leverages the power of OpenAI API and LangChain to provide meaningful and actionable insights. 

## Features

### Code Review

Enter your code into the provided text area and hit the review button. Our backend system, powered by the OpenAI API, will provide instant and useful feedback about your code.

### JD Analyzer

Simply paste the job description into the specified text area and the app will analyze and provide essential keyword insights about the job description.

## Installation

To get started with the app, you need to have Python 3.7 or above. Follow the steps below:

```bash
git clone <repo-url>
cd <project-dir>
pip install -r requirements.txt
streamlit run app.py
```

## Technology Stack
- Python: Python is our primary programming language for this application.
- Streamlit: Streamlit is used for creating the interactive web frontend for the application.
- LangChain: We use LangChain for sophisticated language processing tasks.
- OpenAI API: We use the OpenAI API for complex language model predictions, which help in analyzing code and job descriptions.

## Contribution
We welcome contributions to the project. Please feel free to open an issue or submit a pull request.