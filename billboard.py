import csv
from bs4 import BeautifulSoup as soup

with open('billboard.html', 'r') as file:
        html = file.read()


page = soup(html, 'html.parser')

container = page.find_all('span', class_="chart-element__information")


rank_numbers = page.find_all('span', class_="chart-element__rank__number")

ranks = list()
for rank in rank_numbers:
    ranks.append(rank.get_text().strip())

titles = [title.find('span', class_="chart-element__information__song text--truncate color--primary").get_text().strip() for title in container]

artists = [artist.find('span', class_="chart-element__information__artist text--truncate color--secondary").get_text().strip() for artist in container]

last_week = [week.find('span', class_="chart-element__information__delta__text text--last").get_text().strip() for week in container]

peaks = [peak.find('span', class_="chart-element__information__delta__text text--peak").get_text().strip() for peak in container]

periods = [period.find('span', class_="chart-element__information__delta__text text--week").get_text().strip() for period in container]



for i in range(100):
    template = f'''
Rank: {ranks[i]}
Artist: {artists[i]}
Title: {titles[i]}
Highest rank: {peaks[i]}
Weeks lasted: {periods[i]}
'''
    print(template)


with open('billboard.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Rank', 'Artist', 'Title', 'Highest rank', 'Weeks lasted'])
    for i in range(100):
        csv_writer.writerow([ranks[i], artists[i], titles[i], peaks[i], periods[i]])
