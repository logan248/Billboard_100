import requests
from bs4 import BeautifulSoup as bs


url = 'http://www.todaytvseries2.com/'

request = requests.get(url)

page = bs(request.content, 'html.parser')
print(page.prettify())

file_name = 'today_tv_series.html'

with open(file_name, 'w') as f:
    f.write(page.prettify())
    print('done')
