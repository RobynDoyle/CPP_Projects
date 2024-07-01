from bs4 import BeautifulSoup 
import requests
import pandas as pd
import time 

# Define the URL of the website you want to scrape
url = "https://www.formula1.com/en/results.html/2023/races/1141/bahrain/race-result.html"


# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    print("200")

# set up html for scraping     
soup = BeautifulSoup(response.content, 'html.parser')

#print(soup)

# find table for scraping
table = soup.find_all("table")
column = table

print(table)





"""
#pass to data frame
df = pd.DataFrame(SME_list)
#print(df)
df.to_excel('file path', index = False)

"""
