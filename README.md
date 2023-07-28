# LaunchHacks-Hackaton-ML
## Project: Gaming Review Analysis

## Team Members: 
### [name here], [name here], Brandon Bayquen

## Description:
Python Machine-Learning project for LaunchHacks Hackathon, Summer 2023.

- This consists of a [Metacritic](https://www.metacritic.com/) game-reviews sentiment analyzer

- The program is divided into 2 parts: **Web-Scrapping** and **Sentiment Analysis**
#### The Web Scrapping involves:
1)  Inserting the path of a given Metacritic review URL for a video game (e.g. "game/pc/cyberpunk-2077")
2)  Web-scrapping that URL's HTML pages to retrieve all available USER REVIEWS
3)  Converting the reviews dataset into a *.csv* file
#### The Sentiment Analysis involves:
1)  Using the game-reviews dataset and cleaning its data for useability
2)  Splitting the dataset into two subsets: "positive" and "negative" reviews
3)  Analyzing the file using data processing (i.e. Pandas, etc.) and machine-learning libraries (i.e. Wordcloud, etc.) to find the most repeated words in the datasets
4)  Then generating a corresponding "word cloud" image for each split dataset that showcases the most used words in the reviews.

## How To Use Our Program:
1. First you must have Python3 (v. 3.8 stable build or higher recommended) and Jupyter Notebook installed on your machine:

- LINUX:
```
sudo apt install jupyter-notebook
sudo apt install python3
```
- WINDOWS:
```
pip install jupyter-notebook
# [To install Python for Windows, go to *https://www.python.org/downloads/*]
```
- MAC:
[mac instructions here]
  
2. After running make, you have to install Python package requirements using a command line (e.g. Your machine's terminal, Anaconda, etc):
* To install the package requirements and their dependencies for your machine:

- NOTE: IF you're on Linux (or using Ubuntu 18.04 or higher), INSTALL pip first:
```
sudo apt update
sudo apt install python3-pip
```
Confirm pip installation by checking the pip version:
```
pip3 --version
```

3.  To install the required packages and dependencies:
```
pip install -r requirements.txt
```
* If using Jupyter, to install requirements inside a Jupyter Notebook kernel, open *first_time_installer.ipynb* and run the notebook.

4.  Then to run the program, type the following on your terminal:
```
python3 server.py
```
5.  To use the program:
- Open the page *127.0.0.1:5000* in your browser, then follow the instructions on the HTML page.
