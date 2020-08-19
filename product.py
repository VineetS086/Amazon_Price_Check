from soup import*
import time
#import json
    
class Product():
    def __init__(self, url):
        self.url = url
        self.soup = page_soup(url)
        self.title = title()
        self.price = price()
        self.price_cur = price_cur()
        self.rating = ratings()
        
    
    def details(self):
        return({'time_added': time.ctime(),
                'time_updated': time.ctime(),
                'time_checked': None,
                'url' : self.url,
                'title' : self.title,
                'in_stock': bool(self.price),
                'price' : [self.price,self.price_cur],
                'rating': self.rating,
                'flag_0': False,
                'history':[]
                })
    
