import requests  # Required for making HTTP requests to fetch web pages
from bs4 import BeautifulSoup  # Required for parsing HTML content
import re  # Required for performing regular expression operations (not used here but can be useful)
import pandas as pd  # Required for handling data and saving it as CSV

# Define the URL of the webpage to scrape
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url)  # Make a GET request to fetch the webpage content

soup = BeautifulSoup(r.text,"lxml")  # Parse the webpage content using BeautifulSoup

# Extract names of products
prod = soup.find_all('a', class_="title")
product_names = []

for i in prod:
    name = i.text  # Extract the text content of the product name
    product_names.append(name)

#print(product_names)

# Extract product prices
price = soup.find_all("h4", class_="price float-end card-title pull-right")
prices = []

for i in price:
    b = i.text  # Extract the text content of the price
    prices.append(b)

#print(prices)

# Extract product ratings
rating = soup.find_all("p", class_="review-count float-end")
ratings = []

for i in rating:
    c = i.text  # Extract the text content of the rating
    ratings.append(c)
#print(ratings)    

# Create a DataFrame using the extracted data
df = pd.DataFrame({"Names": product_names, "prices": prices, "Ratings": ratings})

print(df)  # Print the DataFrame to verify extracted data

df.to_csv("product_details.csv")  # Save the extracted data to a CSV file