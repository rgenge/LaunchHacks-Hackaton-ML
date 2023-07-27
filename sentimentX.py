# For Fallout 4 Ratings sentiment analysis with WordCloud!
import numpy as np
import langdetect
#import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import re
import utils
from utils import *
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Read the data:
df = pd.read_csv('fallout4ratings.csv', lineterminator='\n')
print(df.head())

df = df[['Rating', 'Review\r']]
print(df.head())
# Split data by reviews types:
print(f'Positive >= 7: {len(df.loc[df["Rating"] >= 7])}')
print(f'Negative <= 5: {len(df.loc[df["Rating"] <= 5])}')
print(f'5 < Neutral < 7: {len(df.loc[(df["Rating"] > 5) & (df["Rating"] < 7)])}')

# Exclude big reviews (more than 3,000 chars):
long_reviews = df.loc[df["Review\r"].str.len() > 3000].index
df.drop(long_reviews, inplace=True)
print(len(df.loc[df["Rating"] < 100]))
print(df.head(50))

# Let's analyze data of positive reviews:
positive_reviews=df[df['Rating']>=7]
russian_characters = re.compile(r"[\u0400-\u052F]")
cleaned_reviews = []
print(positive_reviews['Review\r'])
# Cleaning data so there is only English reviews to analyze:
for review in positive_reviews['Review\r']:
#    cleaned_review = russian_characters.sub("", review)
#    cleaned_reviews.append(cleaned_review)
    try:
        lang = langdetect.detect(review)
    except:
        continue
    if lang == "en":
      cleaned_reviews.append(review)

words = []
# Split reviews strings in tokes(words):
for value in cleaned_reviews:
    for word in re.split(" ", value):
        if word:
            words.append(word)
# Get a dictionary with all reviews words:
repeated_words = word_count(words)
# Open a file with words that are not important for analysis
entries = set(open('words.txt').read().split())
# Remove all prepositions, pronounms and words that should be analyzed:
entries_to_remove(entries, repeated_words)
repeated_words = (sorted(repeated_words.items(),reverse=True, key=lambda item: item[1]))
# List with the most repeated words:
for i in range(30):
    print(repeated_words[i])
# Cloud with positive reviews words:
word_cloud(positive_reviews['Review\r'],'black','Most Used Words')
# Show our WordCloud image:
plt.show()