from product import Product
import json
import time


def del_history():
    global data
    for p in data['Products']:
        p['history'] = []
    write_data()

def del_all_product():
    l = len(data['Products'])
    print(l)
    for indx in range(l):
        del_product(0)

def del_product(indx):
    del data['P_urls'][indx]
    del data['Products'][indx]
    write_data()
    
def update_all_product():
    global data
    data["Time"] = [time.time(),time.ctime()]
    for indx in range(len(data['Products'])):
        update_product(indx)

def update_product(indx): #update product
    global data
    url = data['P_urls'][indx]
    p_details = Product(url).details()  #{product} main dict
    print('Updating product ',indx)
    
    pro_ = data['Products'][indx]
    
    pro_["time_checked"] = time.ctime()
    if pro_["price"][0] != p_details["price"][0] or pro_["rating"][0] != p_details["rating"][0]:
        change = {'time':pro_['time_updated'],
                  'in_stock': pro_['in_stock'],
                  'price':pro_["price"][:],
                  'rating':pro_["rating"][:]}
        pro_['history'].append(change)
        
        pro_['time_updated'] = time.ctime()
        pro_['in_stock'] = p_details["in_stock"]
        pro_["rating"] = p_details["rating"]
        pro_["price"] = p_details["price"]
        pro_["flag_0"] = True
        

    write_data()
    
    
def write_data():
    global data
    with open('cache.txt','w') as fhand:
        fhand.write(json.dumps(data, indent = 4))

def add_new(url):
    p_details = Product(url).details()    #{product}
    global data
    data['Products'].append(p_details)
    data['P_urls'].append(p_details['url'])
    write_data()
    
def run(url):
    global data
    if url not in data['P_urls']:
        add_new(url)
    else:
        indx = data['P_urls'].index(url)
        update_product(indx)

with open('cache.txt') as fhand:
    data = json.loads(fhand.read()) 
 
 #adds new or updates old one
#print(json.dumps(Product(url).details(),indent = 4))
#del_product(0) #delets