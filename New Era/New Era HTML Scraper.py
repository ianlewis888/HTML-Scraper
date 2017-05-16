from lxml import html
import requests
import csv

SKUs = []

page = requests.get("http://localhost:8080/NewEra.html")
tree = html.fromstring(page.content)
data = tree.xpath('//div[@class="product"]/@id')
print(data)

for product in data:
    SKUs.append([product[8:]])

print(SKUs)

with open('output.csv','w',newline='') as csvfile:
    writeCSV = csv.writer(csvfile, delimiter=',')
    for SKU in SKUs:
        writeCSV.writerow(SKU)

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
