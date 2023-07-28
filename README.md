# LaunchHacks-Hackaton-ML
## Project: Gaming Review Analysis

## Team Members: 
### [name here], [name here], Brandon Bayquen

## Description:
Python Machine-Learning project for LaunchHacks Hackathon, Summer 2023.

- This consists of a [Metacritic](https://www.metacritic.com/) game-reviews sentiment analyzer

- The program is divided into 2 parts: **Web-Scrapping** and **Sentiment Analysis**
#### The Web Scrapping involves:
1)  First, inserting the path of a given Metacritic review URL for a video game (e.g. "game/pc/cyberpunk-2077")
2)  Web-scrapping that URL's HTML pages to retrieve all available USER REVIEWS
3)  Converting the reviews dataset into a *.csv* file
#### The Sentiment Analysis involves:
1)  Using the game-reviews dataset and cleaning its data for useability
2)  Splitting the dataset into two subsets: "positive" and "negative" reviews
3)  Analyzing the file using data processing (i.e. Pandas, etc.) and machine-learning libraries (i.e. Wordcloud, etc.) to find the most repeated words in the datasets
4)  Finally, generating a corresponding "word cloud" image for each split dataset that showcases the most used words in the reviews.

## GUIDE: How To Use Our Program:
1. Please clone this repo locally into your machine in your desired directory.
2. Now, you must have Python 3 (v. 3.8 stable build or higher recommended) and Jupyter Notebook installed on your machine:

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
  
3. After running make, you have to install Python package requirements using a command line (e.g. Your machine's terminal, Anaconda, etc):
* To install the package requirements and their dependencies for your machine:

- NOTE: If you're on LINUX (or using Ubuntu 18.04 or higher), please make sure to INSTALL pip first:
```
sudo apt update
sudo apt install python3-pip
```
Then confirm that pip was installed correctly by checking the pip version:
```
pip3 --version
```

4. To install the required packages and dependencies through a terminal:
```
pip install -r requirements.txt
```
- OR, using Jupyter, install the requirements inside a Jupyter Notebook kernel by opening *first_time_installer.ipynb* and then running it.

5. Type the following on your terminal to run the *server.py* source code:
```
python3 server.py
```
6.  To use the sentiment analyzer:
- Open the page *127.0.0.1:5000* in your browser, then follow the instructions on the HTML page.
