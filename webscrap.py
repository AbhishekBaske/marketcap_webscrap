from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

# URL to be scraped

url = 'https://companiesmarketcap.com/'

# Make a GET request to fetch the raw HTML content

html_content = requests.get(url).text

# Parse the html content

soup = BeautifulSoup(html_content, "lxml")
#print(soup.prettify())  # print the parsed data of html

# scrap division tag with class name `company-name`

company_names = soup.findAll("div", attrs={"class": "company-name"})
market_cap = soup.findAll("td", attrs={"class": "td-right"})

# getting inner text of the division tag

company_name = [name.text for name in company_names]
market_cap = [cap.text for cap in market_cap]
cap = []
price = []

length_cap = len(market_cap)
for i in range(1, length_cap, 3):
    cap.append(market_cap[i])

for i in range(2, length_cap, 3):
    price.append(market_cap[i])

print(len(cap))

for i , j ,k in zip(company_name, cap, price):
    print(i, j, k)

# creating a csv file using pandas
df = pd.DataFrame({'Company Name': company_name, 'Market Cap': cap, 'Price': price})
df.to_csv('company.csv', index=False, encoding='utf-8')
data_dict = df.to_dict('records')

# Save dictionary as JSON
with open('company.json', 'w', encoding='utf-8') as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=4) 


