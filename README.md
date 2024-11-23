# Data Extraction from Wikipedia

##Overview

This project is a Python-based script designed to extract and process data from Wikipedia articles. It uses the wikipedia-api package to perform simple queries and retrieve content in a structured format.

##Features

	•	Install and utilize the wikipedia-api library for querying Wikipedia.
	•	Extract specific sections or summaries of Wikipedia articles.
	•	Process and format the extracted data for further use.

##Getting Started

##Prerequisites

	•	Python 3.6 or later
	•	Installed Python libraries:
	•	wikipedia-api
	•	requests (for HTTP requests)

You can install the required dependencies by running:

pip install wikipedia-api requests

Running the Notebook

	1.	Open the Data_extraction_wiki.ipynb file in a Jupyter Notebook or compatible environment.
	2.	Execute the cells sequentially:
	•	Step 1: Install dependencies.
	•	Step 2: Import the required libraries.
	•	Step 3: Test data extraction by querying a sample Wikipedia page.
	3.	Modify the extraction query parameters to retrieve information about specific topics.

##Project Structure

	•	Part 1: Dependency installation (wikipedia-api and others).
	•	Part 2: Setup and test simple Wikipedia data extraction.
	•	Part 3: Advanced filtering and data formatting for extracted information.
	•	Part 4: Save or process the extracted content for further applications.

##Example Use Case

An example of extracting a summary of the “Python (programming language)” Wikipedia page:

import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')
page = wiki_wiki.page('Python (programming language)')
print(page.summary)

##Contributing

Contributions are welcome! Please create a pull request or raise an issue for feedback and suggestions.

License

This project is licensed under the MIT License. See the LICENSE file for details.
