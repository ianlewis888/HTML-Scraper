from lxml import html
import requests
import csv

prices = []

with open('Swim Product Urls Test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row[2])
        page = requests.get(row[2])
        tree = html.fromstring(page.content)
        price = tree.xpath('//span[@class="textPrice"]/text()')
        print(price)
        prices.append(price)

with open('output prices 2.csv','w',newline='') as csvfile:
    writeCSV = csv.writer(csvfile, delimiter=',')
    for price in prices:
        writeCSV.writerow(price)

#print(prices)

#imageURLs = []

#with open('Swim Product Urls.csv') as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    for row in readCSV:
        #print(row[2])
#        page = requests.get(row[2])
#        tree = html.fromstring(page.content)
#        imageURL = tree.xpath('//img[@id="productMainImage"]/@src')
#        print(imageURL)
#        imageURLs.append(imageURL)

#with open('output_images.csv','w',newline='') as csvfile:
#    writeCSV = csv.writer(csvfile, delimiter=',')
#    for url in imageURLs:
#        writeCSV.writerow(url)
