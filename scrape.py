import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.jumia.com.gh/laptops/'


request = requests.get(url)

page = bs(request.content, 'html.parser')
print(page.prettify())
file_name = 'jumia_laptops.html'

with open(file_name, 'w') as f:
    f.write(page.prettify())
    print('done')
