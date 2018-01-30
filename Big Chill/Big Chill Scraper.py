from lxml import html
import requests
import csv

sizes = []

with open('Input.csv','rU') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        page = requests.get(row[0])
        tree = html.fromstring(page.content)
        width = tree.xpath('//img/@width')
        height = tree.xpath('//img/@height')
        print([width[0], height[0]])
        #sizes.append(price)

#with open('output.csv','w',newline='') as csvfile:
#    writeCSV = csv.writer(csvfile, delimiter=',')
#    for price in prices:
#        writeCSV.writerow(price)
