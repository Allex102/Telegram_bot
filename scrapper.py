import requests as r
from bs4 import BeautifulSoup as bs


def get_url(link=''):
    tv_url = 'https://www.imdb.com/search/title/?title_type=tv_series&count=100'
    movie_url = 'https://www.imdb.com/search/title/?title_type=feature&count=100'
    if link == 't':
        return tv_url
    elif link == 'm':
        return movie_url


def scrapper_func(var):
    result_url = get_url(var)
    response = r.get(result_url)
    soup = bs(response.text, 'html.parser')
    title, year, genre = [], [], []
    data = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
    for i in data:
        n = i.h3.a.text
        title.append(n)

        y = i.h3.find('span', class_='lister-item-year text-muted unbold').text.replace('(', '').replace(')', '')
        year.append(y)

        g = i.p.find('span', class_='genre').text.replace('\n', '').rstrip()
        genre.append(g)

    for x, y, g in zip(title, year, genre):
        print(f'Название : {x}, Год выпуска : {y}, Жанр : {g}', end='\n' * 2)

if __name__ == '__main__':          #Проверка парсера
    scrapper_func('m')
