import requests
import time
import datetime
import random
from bs4 import BeautifulSoup
import pandas as pd
import csv 

url = 'https://www.metacritic.com/game/pc/fall-guys/user-reviews'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    response.raise_for_status()

    # Print response content for debugging
    print(response.content)

    soup = BeautifulSoup(response.text, 'html.parser')
    user_reviews = []

    # Find the HTML elements that contain the user reviews
    review_elements = soup.find_all('li', class_='review')

    # Print the number of review elements found for debugging
    print("Number of review elements found:", len(review_elements))

    for review in review_elements:
        user_info = review.find('div', class_='name')
        user = user_info.find('a').text.strip() if user_info else "N/A"

        date_elem = review.find('div', class_='date')
        date = datetime.datetime.strptime(date_elem.text.strip(), '%b %d, %Y').strftime('%Y-%m-%d') if date_elem else "N/A"

        score_elem = review.find('div', class_='review_grade')
        score = int(score_elem.text.strip()) if score_elem else 0

        review_text_elem = review.find('span', class_='blurb')
        review_text = review_text_elem.text.strip() if review_text_elem else "N/A"


        user_reviews.append({
            'User': user,
            'Date': date,
            'Score': score,
            'Review': review_text
        })

        # Add a random delay between 1 and 2 seconds before the next request
        time.sleep(random.uniform(1, 2))

    # Convert the list of dictionaries into a Pandas DataFrame
    df = pd.DataFrame(user_reviews)
    
    # Drop rows having Nan values 
    df.dropna()
    
    # reset indices 
    df = df.reset_index(drop=True)

    # Save the data to a CSV file
    df.to_csv('fall_guys_user_reviews.csv', index=False)

    print("Reviews scraped and saved successfully.")
except requests.exceptions.RequestException as e:
    print("Failed to fetch the page:", e)
except Exception as e:
    print("An error occurred:", e)



