from lxml import html
import requests
import csv

countries = []

page = requests.get("http://localhost:8080/Options.html")
tree = html.fromstring(page.content)
data = tree.xpath('//option/@value')
print(data)

for country in data:
    countries.append([country])

print(countries)

with open('output.csv','w',newline='') as csvfile:
    writeCSV = csv.writer(csvfile, delimiter=',')
    for country in countries:
        writeCSV.writerow(country)

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
