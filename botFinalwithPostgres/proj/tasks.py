from celery import Celery
from bs4 import BeautifulSoup
import requests
from db import cur

app = Celery('tasks', broker='redis://redis:6379', backend='redis://redis:6379')

@app.task
def parse(URL):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    htmlquantity = 0
    for child in soup.recursiveChildGenerator():
    
        if child.name:

            htmlquantity = htmlquantity + 1
    
    print(URL)
    
    return(htmlquantity)

@app.task
def checkURLinDB(URL):  #if exists return true
    try:
        cur.execute("select * from htmltagsinfo WHERE link = %s ;", (URL,))     #checks if there is any URL in db
        x = cur.fetchall()[0][2]
        return True
    except:
        return False

@app.task
def insertToDB(URL, quant):    #return true is inserted
    try:
        cur.execute("insert into htmltagsinfo (link, tagsquantity) VALUES (%s, %s)", (URL, quant, ))
        return True
    except:
        return False

@app.task
def getQuantityFromDB(URL):
    cur.execute("select * from htmltagsinfo WHERE link = %s ;", (URL,))
    x = cur.fetchall()[0][2]
    return x