from bs4 import BeautifulSoup
from requests import get

def fetch_corona_infection():
    response = BeautifulSoup(get("https://www.worldometers.info/coronavirus/").text, 'html.parser')
    r = list(list(response.find_all('tbody', {'class': 'total_row_body'})[0].children)[1].children)
    i, d = int(r[5].string.replace(',', '')), int(r[9].string.replace(',', ''))
    return i, d
