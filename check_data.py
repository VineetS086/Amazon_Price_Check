from personal import credential
import smtplib
import time
import call_product
import json

def check_changes():
    global list_c
    read_data()
    global data
    for i, product in enumerate(data["Products"]):
        lst = []
        if product['flag_0'] == True:
            product['flag_0'] = False
            if product['history'][-1]['price'][0]!=product['price'][0]:
                lst.append('price')
            if product['history'][-1]['rating'][0]!=product['rating'][0]:
                lst.append('rating')
            list_c.append((i,lst))
    print(list_c)
    write_data()
    
    

def check_time():   #checks time and update
    global data
                    
    if time.time()-data["Time"][0]>600:
        print('Checking Data')
        
        call_product.update_all_product()
        check_changes()
        
    else:
        print('all good')
        

def send_mail(subject,body):
    print('mail')
    credentials = credential()
    email = credentials[0]
    password = credentials[1]
    me = credentials[2]
        
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()                   #No idea
        server.starttls()               #No idea
        server.ehlo()                   #No idea
        server.login(email, password)
    
        msg = f'Subject: {subject}\n\n{body}'
    
        server.sendmail(email, me, msg)
        
def write_data():
    global data
    with open('cache.txt','w') as fhand:
        fhand.write(json.dumps(data, indent = 4))
        
def read_data():
    global data
    with open('cache.txt', 'r') as fhand:
        data = json.loads(fhand.read()) 
        
def run_():
    read_data()
    check_time()
    global list_c, data
    if len(list_c):
        l = len(list_c)
        head = str(l)+" out of "+str(len(data["P_urls"]))+" your wished product(s) has changed their price/rating"
        body = ''
        no_ = 1
        for i in list_c:
            body+= str(no_)+'. '
            no_+=1
            product = data['Products'][i[0]]
            body+= product['title']
            print(i)
        
            if 'price' in i[1]:
                body+= '\n* The price has '
                pri =  product['price']
                pri_ = product['history'][-1]['price']
                p =  float(''.join(pri[0].split(',')))
                p_ = float(''.join(pri_[0].split(',')))
                if p>p_:
                    body+= ('increased from INR '+ pri_[0] +' to INR '+ pri[0] +'.')
                
                elif p<p_:
                    body+= ('decreased from INR '+ pri_[0] +' to INR '+ pri[0] +'.')
                
            if 'rating' in i[1]:
                body+= '\n* The rating has '
                rat = product['rating'][0]
                u = product['rating'][1]
                rat_ = product['history'][-1]['rating'][0]
                u_ = product['history'][-1]['rating'][1]
                r  = float(rat.split()[0])
                r_ = float(rat_.split()[0])
                    
                if r>r_:
                    body+= 'increased from '    
                    
                elif r>r_:
                    body+= 'decreased from '
                body+= rat_.split()[0]+' by '+u+' to '+rat.split()[0]+' by '+u_+'.\n'
            
            body+=('\nVisit Link here: '+product['url'])
            body+='\n-------------------------------------\n\n'
                
        print(head,'\n\n',body)
        send_mail(head,body)
    

list_c = []
data = None

#run_()
