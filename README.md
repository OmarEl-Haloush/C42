Dear Calender 42,

First of all I have never worked with Server connections before, so I had to discover this as I went along with the assignment.
Most of my time was spend understanding getting the information from the server, this is way I chose to used the request libary from Python.
(Since I have never worked with Django before and have the most experience with Python, I chose Python to do the assignment.)

As a standard I import the libary system to access the arbitary functions of reading and writing to files 
as to be able to get information from the calling line once a programm is started (the latter is not implemented in the code).

In order to furfill the request of limmiting the data usage and the 4.2 minutes time out, the time libary is used.

To use the code download the files ApiC42.py and idclass.py and start ApiC42.py, or copy the code from Github. 
The code uses default parameters, but allows for changes in the options.

After retrieving the data from your server I ran into the problem of Unicode. 
I was unable to find documentation for easy handeling of Unicode in Python. This is why I created the idclass insctance (idclass.py).
I chose to handle this part of the code in a seperate document to keep the code organized. This code is accessed by calling the datahandler function
and will return the recieved information from the sever as idclass instances. This allows the user to have an easy access to the information
of the subscribers and me being able the furfull the assignment. 

The idclass allows for further processing of the data from the server if desired, although this is not implemented at the time.

The end result of the code is found in the file output.txt which is created after running the code for the first time.
The result is also printed on the screen for a fast feedback. 
The difference between the 4.2 timeout or retrieving the data once more is an aditional enter between the printed lines on screen.

I hope this is meeting the demands of the information you desired in the README.md

Kind regards,
Omar El-Haloush



