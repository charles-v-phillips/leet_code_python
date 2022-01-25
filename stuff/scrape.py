from bs4 import BeautifulSoup as bs
import requests
import csv

request = requests.get('https://www.prisonpolicy.org/origin/ny/police_precincts.html')
soup = bs(request.text,'html.parser')
print('hi')
table = soup.find(attrs = {"id": "table_appendix"})

rows = table.find_all(name="tr")
rows = rows[1:]

with open("precinct_population.csv", 'w') as f:
    writer = csv.writer(f)
    headers = ["precinct","pop"]
    writer.writerow(headers)
    s = 0
    for r in rows:
        print(r)
        info = r.text.split(" ")
        prec = int(info[0])
        pop = int(info[2].replace(",", ""))
        s+=pop
        writer.writerow([prec,pop])
    print(f's = {s}')

if __name__ == '__main__':
    pass




