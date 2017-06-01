from lxml import html
import requests
import csv

productIds = []

with open('Input.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row[0])
        page = requests.get(row[0])
        tree = html.fromstring(page.content)
        productId = tree.xpath('//input[@name="productId"]/@value')
        en = "EN" + str(productId[0])
        fr = "FR" + str(productId[0])
        productIds.append([en, fr])

print(productIds)

with open('output.csv','w',newline='') as csvfile:
    writeCSV = csv.writer(csvfile, delimiter=',')
    writeCSV.writerow(["English","French"])
    for productId in productIds:
        writeCSV.writerow(productId)
