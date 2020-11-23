import requests
import json



def send_sms(number,message) :
    url = "https://www.fast2sms.com/dev/bulk"
    pararmeters = {
        'authorization' : 'GSazVyRwvTtQD3lBPOniEoAkFUL8bYrfexdHc9Ku1qMXg5CIm4UCXJ7Ns4gcQofqxhDZzHMvLIda6KBr' ,
        'sender_id' : 'fast2sms' ,
        'message' : message ,
        'language' : 'english' ,
        'route' : 'p' , 
        'numbers' : number , 
    }

    response = requests.get(url,pararmeters)
    response = response.json()
    print(response) 


number  = input("Enter the number you want to send the sms to : ")
message = input("Enter the message you want to send : ")

send_sms(number,message)