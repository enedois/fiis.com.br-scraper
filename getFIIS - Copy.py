from urllib.request import urlopen, Request
from pyquery import PyQuery as pq
import lxml, lxml.html
from lxml import etree
import os
import datetime
import threading

##carrega os papeis de stocksList.csv
stocksList = open('FIIsList.csv', 'r')
#papeis = stocksList.read().split(';')
papeis = ["xppr11"]
stocksList.close()

## pegando o dia e mês
now = datetime.datetime.now()
dia = now.day-1
mes = now.month
data = str(dia)+"."+str(mes)
threads = []

## cria diretorio para a data de hoje-1
if (not os.path.isdir('./'+data)):
    os.mkdir(data)

#def faltam(papeis):
    #print(len(papeis))

def getpapel(papel_):
    try:
                    url = "https://fiis.com.br/"
                    #print(papel+": "+str(content.code))
                    r = Request(url+papel_, headers={'User-Agent': 'Mozilla/5.0'})
                    html = urlopen(r).read()
                    query = pq(html)
                    #print(conteudo)
                    head = query("thead").html()
                    content = query("tbody").html()
                    #print(head)
                    #print(content)
                                       
                    head = head.replace("<td>","").replace("</td>","")
                    content = content.replace("<td>","").replace("</td>","")
                    print(head)
                    print(content)
                    
                    papeis.remove(papel_)
                    
                    
                    
    except Exception as e:
        print("#ERRO: ",papel," ", str(e))
        papeis.remove(papel_)
        #print(papeis)
    

while len(papeis)>0:
    for papel in papeis:
        getpapel(papel)
            


