from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

##carrega os papeis de stocksList.csv
stocksList = open('AllFiis.csv', 'r')
papeis = stocksList.read().split(';')
stocksList.close()


def getpapel(papel_):
    try:
                    url = "https://fiis.com.br/"                    
                    r = Request(url+papel_, headers={'User-Agent': 'Mozilla/5.0'})
                    html = urlopen(r).read()
                    soup = BeautifulSoup(html, 'html.parser')                    
                    result = soup.find_all('tr')
                    alldata = []
                    for row in result:                        
                        columns = (row.get_text().replace("\n", " ").replace("R$ ", "").strip().split(" "))
                        alldata.append(columns)
                        print(papel_+"|"+columns[1]+"|"+columns[4])                        
                    papeis.remove(papel_)
                    
                    
    except Exception as e:
        print("#ERRO: ",papel," ", str(e))
        papeis.remove(papel_)   

while len(papeis)>0:
    for papel in papeis:
        getpapel(papel)
            


