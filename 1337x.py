#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

from bs4 import BeautifulSoup as soup

with open('1337x_today.html', 'r') as html_file:
    html = html_file.read()

page = soup(html, 'html.parser')

container = page.find_all('tr')
del container[0] 

rating = [rate.find('span', class_="rating-text").get_text().strip() for rate in container]

titles = [title.find('a').get_text().strip() for title in container]

links = [link.find('a')['href'] for link in container]

seeds = [seed.find('td', class_="coll-2 seeds").get_text().strip() for seed in container]

leeches = [leech.find('td', class_="coll-3 leeches").get_text().strip() for leech in container]

dates = [date.find('td', class_="coll-date").get_text().strip() for date in container]


url = '1337x.to'

#for i in range(len(rating)):
#    template = f'''
#Rating: {rating[i]}
#Title: {titles[i]}
#Seeds: {seeds[i]}
#Leeches: {leeches[i]}
#Date: {dates[i]}
#Link: {url}{links[i]}'''
#    print(template)

with open('1337x.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    fieldnames = ['Rating', 'Title', 'Seeds', 'Leeches', 'Date', 'Link']
    csv_writer.writerow(fieldnames)

    for i in range(len(titles)):
        link = f'{url}{links[i]}'
        csv_writer.writerow([rating[i], titles[i], seeds[i], leeches[i], dates[i], link])

print('done')
