from lxml import html
import requests
import csv
import sys
v = sys.version
reload(sys)
sys.setdefaultencoding('utf-8')
data = [['Date','Time','Location','Operator','Flight Number','Route','Aircraft Type',\
    'Registration','cn/ln','Aboard','Fatalities','Ground','Summary']]
og_page = requests.get("http://www.planecrashinfo.com/database.htm")
og_tree = html.fromstring(og_page.content)
years = og_tree.xpath('//td[@width="55"]/strong/a/@href')
years[9] = "/"+years[9]
print(years)

for year in years:
    year_int = year.split('/')[1]
    page = requests.get("http://www.planecrashinfo.com"+year)
    tree = html.fromstring(page.content)
    crashes = tree.xpath('//td/font/a/@href')
    print(crashes)

    for i in crashes:
        p1 = requests.get("http://www.planecrashinfo.com/"+year_int+"/"+i)
        p2 = html.fromstring(p1.content)
        crash = p2.xpath('//table/tr/td[2]/font/text()')
        data.append(crash)
        print(crash)

with open('Plane Crash Data/output.csv','wb') as csvfile:
    writeCSV = csv.writer(csvfile, delimiter=',')
    for crash in data:
        writeCSV.writerow(crash)
