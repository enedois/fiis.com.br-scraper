from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

##carrega os papeis de stocksList.csv
stocksList = open('ifix.csv', 'r')
papeis = stocksList.read().split(';')
##papeis = ["VRTA11"]
stocksList.close()


def getpapel(papel_):
    try:
                    url = "https://fiis.com.br/"                    
                    r = Request(url+papel_, headers={'User-Agent': 'Mozilla/5.0'})
                    html = urlopen(r).read()
                    ##print(html)
                    soup = BeautifulSoup(html, 'html.parser')                    
                    result = soup.find_all("div", class_="indicators__box")
                    ##print(len(result))
                    alldata = []
                    

                    print(papel+" "+re.sub('\s+',' ',result[0].text.strip()))
                    ##for row in result:
                        ##print(row.text)                        
                                              
                    papeis.remove(papel_)
                    
                    
    except Exception as e:
        print("#ERRO: ",papel," ", str(e))
        papeis.remove(papel_)   

while len(papeis)>0:
    for papel in papeis:
        ##print("Procurando papel "+papel)
        getpapel(papel)
            


