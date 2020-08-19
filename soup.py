from bs4 import BeautifulSoup
import requests
from personal import user_agent  #varies..... DELETE IT BEFORE SHARING
import re
pc = None
soup = ''

def page_soup(url):
    global soup
    header = {'User-Agent' : user_agent()}
    page_h = requests.get(url , headers = header)
    soup = BeautifulSoup(page_h.content, 'html.parser')
    return soup

def title():
    global soup
    try:
        t = soup.find(id = 'productTitle').get_text().strip()
    except:
        t = 'None'
    return t

def price():
    global pc
    global soup
    try:
        try:
            p = soup.find(id = 'priceblock_ourprice').get_text()
            
        except:
            p = soup.find(id = 'priceblock_dealprice').get_text()
        p = p[1:].strip()
    except:
        p = None
        
    return p

def price_cur():
    try:
        global soup
        text = str(soup.find(id = 'cerberus-data-metrics'))
        c = re.findall(r'data-asin-currency-code..(...)',text)[0]
    except:
        c = None
    return c
    
def ratings():
    try:
        global soup
        count = soup.find(id = 'acrCustomerReviewText').get_text().split()[0]
        tags = soup.find_all('span')
        tag = [t for t in tags if 'rating-out-of-text' in str(t)][0]
        rating = tag.get_text()
    except:
        rating,count = 'None','None'
    
    return(rating,count)
    
