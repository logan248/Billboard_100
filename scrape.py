import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.imdb.com/?mode=desktop&ref_=m_ft_dsk'


request = requests.get(url)

page = bs(request.content, 'html.parser')
print(page.prettify())

file_name = 'imdb.html'

with open(file_name, 'w') as f:
    f.write(page.prettify())
    print('done')
