#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
from bs4 import BeautifulSoup as soup

filename = 'today_tv_series.html'

with open(filename, 'r') as html_file:
    html = html_file.read()

page = soup(html, 'html.parser')

new_series_container = page.find_all('li', class_="tm-tag-10")

new_series = [new.find('span', class_='uk-float-left').get_text().strip() for new in new_series_container]

new_series_month = [mon.find('span', class_='uk-float-right').get_text().strip() for mon in new_series_container]

new_series_title = [title.find('h3').get_text().strip() for title in new_series_container]

new_series_summary_container = page.find_all('div', class_="uk-article-lead")

new_series_summary = [summary.find('p').get_text().strip() for summary in new_series_summary_container]

new_series_link = page.find_all('a', class_="uk-margin-top uk-button uk-button-link")
link = [link['href'] for link in new_series_link]

http = 'http://www.todaytvseries2.com'

container = page.find_all('div', class_="uk-panel uk-panel-box uk-panel-box-primary uk-invisible")
print(container[0])

rough_dates = [date.find('div', class_="dateEpisode").get_text().strip() for date in container]

dates = list()
episodes = list()

for date in rough_dates:
    new_date = date.split('\n')
    episode = new_date[0].strip()
    clean_date = new_date[-1].strip()
    episodes.append(episode)
    dates.append(clean_date)


titles = [title.find('a', class_="uk-link-reset").get_text().strip() for title in container]
links_trend = [link.find('a', class_="uk-button") for link in container]
true_links = [link['href'] for link in links_trend]

with open('series.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Series', 'Release date', 'Title', 'Summary', 'Link'])

    for i in range(len(new_series_title)):
        new_link = f'{http}{link[i]}'
        fieldnames = [new_series[i], new_series_month[i], new_series_title[i], new_series_summary[i], new_link]
        csv_writer.writerow(fieldnames)

    csv_writer.writerow(['Series', 'Release date', 'Title', 'Link'])

    for j in range(len(titles)):
        new_link = f'{http}{true_links[j]}'
        fieldnames = [episodes[j], dates[j], titles[j], new_link]
        csv_writer.writerow(fieldnames)



