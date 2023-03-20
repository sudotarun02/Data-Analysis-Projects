import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

rank, name, year, rating = [], [], [], []

try:
    response = requests.get(url)
    response.raise_for_status()

    page = BeautifulSoup(response.text, 'html.parser')

    movies = page.find('tbody', class_="lister-list").find_all('tr')

    for movie in movies:
        rank.append(movie.find('td', class_="titleColumn").get_text(
            strip=True).split('.')[0])
        name.append(movie.find('td', class_="titleColumn").a.text)
        year.append(movie.find(
            'td', class_="titleColumn").span.text.strip('()'))
        rating.append(movie.find(
            'td', class_="ratingColumn imdbRating").strong.text)

except Exception as e:
    print(e)

data = {'Rank': rank, 'Name': name, 'Year': year, 'Rating': rating}
df = pd.DataFrame(data)
print(df.head(10))
#df.to_csv('IMDB Movies.csv', index=False)
