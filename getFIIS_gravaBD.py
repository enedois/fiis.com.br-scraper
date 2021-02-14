from urllib.request import urlopen, Request
from pyquery import PyQuery as pq
import lxml, lxml.html
import os
import datetime
from bs4 import BeautifulSoup
import pandas
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fii-data"
)

##carrega os papeis de stocksList.csv
stocksList = open('FIIsList.csv', 'r')
papeis = stocksList.read().split(';')
print(papeis)
#papeis = ["xppr11"]
stocksList.close()

while len(papeis)>0:
    for papel in papeis:
        getpapel(papel)

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
                        
                    alldata.pop(0)#remove o cabecalho
                    
                    for row in alldata:
                        print(papel_+" / "+row[1]+" / "+row[4])
                        data_atual = datetime.datetime.strptime(row[1], "%d/%m/%y")
                        #grava no banco de dados
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO `dividendo-data`(`fii_nome`, `data_pagamento`, `valor_dividendo`) VALUES (%s, %s, %s)"
                        val = (papel_,data_atual, float(row[4].replace(",",".")))
                        mycursor.execute(sql, val)
                        mydb.commit()
                        #print(data_atual.month)

                    print("Removendo o papel "+papel_+" Faltam "+str(len(papeis)))
                    papeis.remove(papel_)
                    
                    
    except Exception as e:
        print("#ERRO: ",papel_," ", str(e))
        print("Removendo o papel "+papel_+" Faltam "+str(len(papeis)))
        papeis.remove(papel_)
        #print(papeis)
    


            


