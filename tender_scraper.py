# Import necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests


class Scraper:
    # Type in url which has to be accessed
    def __init__(self):
        self.url = "https://etenders.gov.in/eprocure/app"

    # Get content of website
    def scrape_data(self):
        response = requests.get(self.url)
        html_content = response.text

        # Create a BeautifulSoup object by parsing the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the table element
        table = soup.find('table', id='activeTenders')

        # Enter table data into list and save it in dataframe
        if table is not None:
            rows = table.find_all('tr')

            data = []
            data.append(['a', 'b', 'c', 'd'])
            for row in rows:
                columns = row.find_all('td')
                row_data = [column.text.strip() for column in columns]
                data.append(row_data)

            df = pd.DataFrame(data[1:], columns=data[0])

        else:
            print("Table not found on the webpage")

        # Exporting data into csv

        df.to_csv('activetenders.csv')

        # read contents of csv file
        file = pd.read_csv("activetenders.csv")
        print(file)

        # adding header
        headerList = ['tender title', 'id', 'closing date', 'opening date']

        # Converting data frame to csv and remove first column

        file = file.iloc[:, 1:]

        # Export back into csv
        file.to_csv("activetenders.csv", header=headerList, index=False)
