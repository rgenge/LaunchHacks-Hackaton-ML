# LaunchHacks-Hackaton-ML
## Project: Sentiment Analysis

## Team members: 
### [name here], Brandon Bayquen, [name here]

## Description:
Machine Learning project for LaunchHacks Hackathon, Summer 2023.

- This consists of a Metacritic game-reviews sentiment analyzer

- The program is divided into 2 parts: Web Scrapping and Sentiment Analysis
#### The web scrapping part involves:
1)  Inserting the path of a given game's URL of reviews from Metacritic (e.g. "game/pc/cyberpunk-2077")
2)  Web scrapping the URL's pages and getting all available USER REVIEWS from that game into a *.csv* file
#### The Sentiment analysis involves:
1)  Getting all the data, cleaning it, and getting the most repeated words to analyze what people like and dislike about it.

## Web Scrapper

This part of the program consists of a program to get all data from a web page by ................


## Sentiment Analysis

This part of the program consists of a program that will read all of dataset .....................


## How to use it?
1. First you must have Python3 and Jupyter Notebook installed:

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
  
2. After running make, you have to install Python requirements using a command line (e.g. Your machine's terminal, Anaconda, etc):
* To install the package requirements and their dependencies for your machine type:
```
pip install -r requirements.txt
```
* If using Jupyter, to install requirements inside a Jupyter Notebook kernel, open *first_time_installer.ipynb* and run the notebook.

3.  Then to run the program:
```
python3 server.py
```
4.  To use the program:
- Open the page *127.0.0.1:5000* and put a path wait and then run it
