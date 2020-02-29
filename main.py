from bs4 import BeautifulSoup as bs
import requests as r

mainlink="https://www.cs.toronto.edu/~vmnih/data/mass_roads/train/map/index.html"

page=r.get(mainlink)
soup=bs(page.content,'html.parser')

links=[]
for link in soup.find_all('a'):
    links.append(link.get('href'))

for l in links:
    ipl=l
    opl=l.replace("sat","map")
    ip=r.get(ipl)
    op=r.get(opl)
    file=l[59:]
    with open('/home/ani/input/'+file,'wb') as f:
        f.write(ip.content)
    with open('/home/ani/output/'+file,'wb') as f:
        f.write(op.content)
    print(file)
