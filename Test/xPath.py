from lxml import html
import requests
import csv

page = requests.get("https://en.wikipedia.org/wiki/List_of_largest_cities")
tree = html.fromstring(page.content)
data = tree.xpath('//table[@style="text-align:right; background-color:white;"]/*/*/a/text()')

print(data)

'''
with open('/Users/ianlewis/Documents/GitHub/HTML-Scraper/Test/output.csv','wb') as csvfile:
    writeCSV = csv.writer(csvfile, delimiter=',')
    for product in feed:
        writeCSV.writerow(product)'''
