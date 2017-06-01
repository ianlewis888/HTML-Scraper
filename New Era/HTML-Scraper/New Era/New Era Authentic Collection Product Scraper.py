from lxml import html
import requests
import csv

page = requests.get("http://shop.neweracap.com/Style/59Fifty-MLB-Authentic-Collection?recs=all")
feed = [['Product ID','Product Name','Product URL','Image URL','Price']]
tree = html.fromstring(page.content)
skuData = tree.xpath('//div[@class="product"]/@id')
urlData = tree.xpath('//div[@class="product"]/a/@href')
nameData1 = tree.xpath('//div[@class="product"]/div/h3[1]/a/text()')
nameData2 = tree.xpath('//div[@class="product"]/div/h3[2]/a/text()')
priceData = tree.xpath('//div[@class="product"]/div/h4/a/text()')

for product in skuData:
    sku = product[8:]
    feed.append([sku, nameData1[skuData.index(product)] + " " + nameData2[skuData.index(product)],\
     "http://shop.neweracap.com" + urlData[skuData.index(product)], \
     "http://lf.lids.com/hwl?set=sku[" + sku + "],c[2],w[400],h[300]&load=url[file:product]",\
     priceData[skuData.index(product)][1::]])

print(feed)

with open('output.csv','wb') as csvfile:
    writeCSV = csv.writer(csvfile, delimiter=',')
    for product in feed:
        writeCSV.writerow(product)
