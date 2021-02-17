from urllib.request import urlopen, Request
from pyquery import PyQuery as pq
import lxml, lxml.html
import os
import datetime
from bs4 import BeautifulSoup
import pandas

##carrega os papeis de stocksList.csv
stocksList = open('FIIsList_Carteira.csv', 'r')
#papeis = stocksList.read().split(';')
papeis = ["xppr11"]
stocksList.close()

## pegando o dia e mês
now = datetime.datetime.now()
dia = now.day-1
mes = now.month
data = str(dia)+"."+str(mes)


## cria diretorio para a data de hoje-1 
#if (not os.path.isdir('./'+data)):
    #os.mkdir(data)

#def faltam(papeis):
    #print(len(papeis))

def getpapel(papel_):
    try:
                    url = "https://fiis.com.br/"
                    #print(papel+": "+str(content.code))
                    r = Request(url+papel_, headers={'User-Agent': 'Mozilla/5.0'})
                    html = urlopen(r).read()
                    soup = BeautifulSoup(html, 'html.parser')
                    #print(soup.prettify())
                    result = soup.find_all('tr')
                    alldata = []
                    for row in result:
                        #print(type(row))
                        columns = (row.get_text().replace("\n", " ").replace("R$ ", "").strip().split(" "))
                        alldata.append(columns)
                        #print(columns)
                        #for column in columns:
                           #print(column)
                    
                    print(papel_+" "+alldata[1][1]+" "+alldata[1][4])
                    data_atual = datetime.datetime.strptime(alldata[1][1], "%d/%m/%y")
                    print(data_atual.month)
                    papeis.remove(papel_)
                    
                    
    except Exception as e:
        print("#ERRO: ",papel," ", str(e))
        papeis.remove(papel_)
        #print(papeis)
    

while len(papeis)>0:
    for papel in papeis:
        getpapel(papel)
            


