import sys

""" 
This document contains the source code to handle the Get request for the assignment. Code needs to be used with ApiC42.py 
in odrder to work as efficiently as possible. Data that is send here from the C42 server is broken appart and put together to furfill
the assignment. But it also facilitates further usages by already putting the data in a idclass,
which contains all the information send from the server. Not all of the data is correctly handeled, 
but it allows the user to acces the most releveant information of the subscribers. 
(Because the data is broken appart time and dates are incorrectly handled at the time, however this is not important for forfilling the assignment)
"""


def  DataHandler(data):
    # This function breaks appart the data and calls on creating a idclass instance for every subscriber in the recieved data from the sever
    
    # Following parameter are used to process the data
    opencounter=0
    start=False
    memopen=0
    closecounter=0
    close=False
    memclose=0
    count=0
    datalist=list()

    #Finding a the subscribers in the data
    for i in range(0,len(data)-1):
        if data[i]=="{":
           opencounter+=1
           # Setting a start point to process a subscriber
           if start==False:
               start=True
               memopen=i
        if data[i]=="}":
            closecounter+=1
            if (opencounter-1)-(closecounter)==0:
                # Setting the end point to process a subscriber
                if close==False:
                    close=True
                    memclose=i
           
        if start==True & close==True:
            # Sending the data from the server from the start to end point to create an idclass
            datalist.append(dataid(data[memopen:memclose]))
            count+=1
            memsopen=0
            memclose=0
            start=False
            close=False
    # Function returns a list containing all processed data in the idclass instance        
    return datalist
 
class dataid:
    # The idclass
    def __init__(self, idinfo):
        # Following parameters are based on the recieved data from each subscriber to make sure all the data is easily accesable to the user
        self.dataid=str()
        self.eventid=str("")
        self.subscriber={"id":"","first_name":"","last_name":"","photo":"","tags":"","email":"","phonenumber":""}
        self.is_invitation=str("")
        self.premission=str("")
        self.actor={"id":"","first_name":"","last_name":""}
        self.message=str("")
        self.created=str("")
        self.calender_id=str("")
        self.rsvp_status=str("")
        self.sync_token=str("")
        
        # Breaking appart the data even further
        idinfo=idinfo.split(":")
        for char in idinfo:
            try:
                char=char.split(",")
            except:
                print("exception on data", char)
                continue
        # Reassembling the data 
        newinfo=list()  
        for info in idinfo:
            newstr=str()
            for char in info:
                if char==",":
                    newinfo.append(newstr)
                    newstr=str()
                    continue
                if char not in ["[",'"',"{","]","}"]:
                    newstr+=char
            newinfo.append(newstr)
            
        # Assigning the paramters of the idclass
        for i in range(0,len(newinfo)-1):
            if newinfo[i]=="id" and self.dataid=="":
                self.dataid=newinfo[i+1]
                continue
            if newinfo[i]=="event_id" and self.eventid=="":
                self.eventid=newinfo[i+1]
                continue
            if newinfo[i]=="subscriber" :
                # Because of aesthetic reasons for the code, this data is handeled in a seperate function
                self.databaseHandler("subscriber", newinfo[i:i+15])
                i+=15
                continue
            if newinfo[i]=="is_invitation" and self.is_invitation=="":
                self.is_invitation=newinfo[i+1]
                continue
            if newinfo[i]=="premission" and self.premission=="":
                self.premission=newinfo[i+1]
                continue
            if newinfo[i]=="actor":
                # Because of aesthetic reasons for the code, this data is handeled in a seperate function
                self.databaseHandler("actor", newinfo[i:i+7])
                i+=7
                continue
        return     
        
        
    def databaseHandler(self, command, info):
        # This function creates an easy access in the subriber parameter of the idclass as a database
        if command=="subscriber":
            for i in range(0,len(info)-1):
                if info[i]=="id":
                    self.subscriber["id"]=info[i+1]
                if info[i]=="first_name":
                    self.subscriber["first_name"]=info[i+1]
                if info[i]=="last_name":
                    self.subscriber["last_name"]=info[i+1]   
                if info[i]=="photo":
                    self.subscriber["photo"]=info[i+1] 
                if info[i]=="tags":
                    self.subscriber["tags"]=info[i+1]    
                if info[i]=="email":
                    self.subscriber["email"]=info[i+1]
                if info[i]=="phonenumber":
                    self.subscriber["phonenumber"]=info[i+1]    
        if command=="actor":
            for i in range(0,len(info)-1):
                if info[i]=="id":
                    self.actor["id"]=info[i+1]
                if info[i]=="first_name":
                    self.actor["first_name"]=info[i+1]    
                if info[i]=="last_name":
                    self.actor["last_name"]=info[i+1]    
        return
    
    def __str__(self):
        # Build in function of Python to display the id's and event id's of the idclass
        string=str("ID : " +self.dataid+'\n'+"Event Id :"+ self.eventid)
        return string