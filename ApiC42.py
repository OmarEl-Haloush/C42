import sys
import requests
import time
from idclass import *

# My identification
event_id1= str("d07a1e290727d3000219590feb5b9590_14698019015091")
token1= str("d790167168617e53d618f3401335ff241a332287")

def TestEvent(event_id, token):
    #Initiate conection
    tnow=time.perf_counter()
    try:
        #Check if the code has been used in the last 4.2 minutes
        file=open("time.txt",'r')
        for line in file:
            tprev=line
        if tnow-float(tprev)<=252:
            file=open("output.txt", 'r')
            for line in file:
                print(line)
            return    
        
    except:
        print("Function used for the first time, creating files...")
    
    
    # Creating custom headers for request
    url=str("https://demo.calendar42.com/api/v2/event-subscriptions/")
    headers= {"event_ids": event_id,"Accept": "application/json", "Content-type": "application/json", "Authorization": "Token "+token,  "globoff":""}
    r=requests.get(url, headers=headers)
    
    # Status check
    if r.status_code==401:
        print("Error on url. Please Check 'Token'")
        return
    if r.status_code==404:
        print("Error on url. Please Check 'event id'")
        return
    
    # Preparing data to handle
    message=str(r.text)
    # Sending data to be handeled (see idclass.py for further information)
    message=DataHandler(message)
     
    def output(output,question="names"):
        # Creates Output on line in screen and output file for further ues
        result=str()
        
        # Formating data in JSOn structure
        result+="{"+'\n'+'"id"'+':'+'"'+event_id+'"'+'\n'+'"title"'+':'+ '"Test Event"'+'\n'+'"'+question+'"'+':'+'['
        for i in range(1,len(output)):
            result+='"'+output[i]+'",'
        result+=']'+'\n'+'}'
        
        # Show data on screen
        print(result)
        
        # Writing data to file for further use
        file=open("output.txt",'w')
        file.write(result)
        
        # Writing intial request time to file to limit data usage
        file=open("time.txt" ,'w')
        file.write(str(tnow))
        
    def finddata(message, question="names"):
        # Function for requesting the desired data
        result=list()
        for dataid in message:
            if question=="names":
                result.append(dataid.subscriber["first_name"])
            else:
                # Option to find other data of subscriber
                result.append(dataid.subscriber[question])
        # Calling of Output function        
        output(result, question) 
        
        # Returning result for immediate excess
        return result
        
    result=finddata(message)
    
# Call to initate Test Event    
TestEvent(event_id1, token1)    