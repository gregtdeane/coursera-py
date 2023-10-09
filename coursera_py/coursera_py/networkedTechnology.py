import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests
import pandas as pd
from IPython.display import display


mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creates endpoint inside my computer that is 
#ready to connect out to far end- IT IS A CONNECTION PT THAT HAS NOT YET BEEN CONNECTED
#Like opening a door
#INET for using internet
#Stream for stream of characters to be expected back
#Creates socket object

mysock.connect(('data.pr4e.org',80))
#actuall connection happens here
#Call connection method on that object
#makes the connection
#like dialing the phone (still not sending any data)

#Every thing above was in the Transport layer - Establishing the transport layer-->Connected to specifc port on another computer
# Next need to working in application layer --> Application protocols
#Application layer- there is something different when talking to a mail server vs www
# First set of application layer commands is like things you say at beginning of phone call
#HTTP is dominant application layer on internet
#basic concept: Make connection --> Request doc --> Retrieve doc --> Close connection

#HTTP is set of rules that allow browsers to retrieve web docs from servers over the internet
#HTTP standardized URL: protocol (http://) , host (www.dr-chuck.com), document (/page1.htm)
#REQUEST RESPONSE CYCLE
#user clicks on anchor tag (href=value), browser makes connection to web server, 'GET' request, 
# server returns HTML doc to browser, browser formats and displays

#Series of standards developed by Internet engineering task force (IETF)
#Document request: e.g. GET http:// www.../page1.htm HTTP/1.0 (GET, URI, protocol)

#telnet --> old, way to connect to any port on any server and send stuff to it
#telnet data.pr4e.org 80 #connect to web server port on the host
#GET http://data.pr4e.org/page1.htm HTTP/1.0 - some web servers are impatient --need to type this fast

#META DATA
#HTTP/1.1 200 OK
#Date: Thu, 08 Jan 
#Last-modified
#Connection: close
#Content-Type: text/html

#BlankLine

#<h1>The First Page </h1> etc..html code for web page

# Trying 192.241.136.170...
# Connected to data.pr4e.org.
# Escape character is '^]'.
# GET http://data.pr4e.org/romeo.txt HTTP/1.0

# HTTP/1.1 200 OK
# Date: Mon, 18 Sep 2023 06:14:53 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "a7-54f6609245537"
# Accept-Ranges: bytes
# Content-Length: 167
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/plain

# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief
# Connection closed by foreign host.
################ WORKED EXAMPLE: SOCKETS ######################
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#encode needed because there are strings inside python that are in unicode --> need to be TXd in UTF-8
#encode converts from unicode to UTF-8
#cmd is UTF-8

mysock.send(cmd)

while True:
    data = mysock.recv(512) #start reveiving data up to 512 characters
    if (len(data)<1):# if we get no data --> EOF or End of transmission
        break
    print(data.decode()) #decode data internally --> converts UTF-8 to unicode
mysock.close()

############### USING DEVELOPER CONSOLE TO EXPLORE HTTP ########################
#In web address can include parameters to be sent to server using "?"
#e.g. number guessing game, send website.../?guess=12
# Web server sees parameters as key:value pairs like a dictionary
# Request can be a POST or GET request

#response contains status code 200-good server/file, 404-Not found, 302 with LOCATION - redirect to another place
# To redirect..send GET/POST request to web server, server responds with 302 status code-"I did not give
# you a document, I gave you a location header, go here instead"

# 
# 
# 

#Unicode Characters and Strings
#Computers dont understand letters - they understand numbers
# So need to develop mappings from letters to numbers
#Common in 1980s ~ASCII
# ASCII is 7 bits (128 possible) 0000000 to 1111111
# "ord('H') " - what is the ascii decimal number corresponding to 'H'
# Issue with ASCII japanese computers coudnt talk to USA computers
# Unicode was invented
# UTF-16 (2 bytes)
# UTF-32 (4 bytes)
# UTF-8 (1-4 bytes)
#   upwards compatible with ASCII
# UTF-8 now most common
# When programming in Python with local files, dont need to worry about character sets because 
# it should match files on the computer but different computers on a network can have different character sets
# After python 3, all character sets are of class "str"
# Byte string - raw data - and we don't know what encoding is 
# In python 3, byte is different class from ascii/utf string
# data.decode() decodes byte string into ascii or utf and can decide which one automatically
# data.decode() converts bytes to unicode
# encode() assumes UTF 8 - converts string to UTF
# decode is a method of "bytes" class, encode is a method of "str" class
# Must encode before send
# program -->   all over port 80 
    # Socket
    # Connect
        # Encode()
    # Send
    # Receive
        # Decode()

# urllib does all the socket work for us and makes web pages look like a file
# import urllib.request, urllib.parse, urllib.error
fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #sorta like open for files
for line in fhandle: #line is a byte array so need to decode
    print(line.decode().strip())
    #Urlopen eats the headers but we can ask for them


#parsing web pages
# Web scraping is writing a python program that automates the sending of get requests and getting data back
# Spidering - web crawling - following sublinks within pages
# Web scraping useful for getting data out of system that has no "export capability"
# Many HTML pages have syntax errors - hardest part of spidering is parsing the HTML
# Browsers have many processes that forgive HTML syntax errors - "We'll just show it"
# Makes it hard to make regex's, filtering
# BeautifulSoup helps to do the same thing that a browser would do with bad HTML syntax

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter -') # try with http://www.dr-chuck.com/page1.htm
# url = 'https://finance.yahoo.com/quote/AAPL231013C00050000?p=AAPL231013C00050000'
# url = 'https://finance.yahoo.com/quote/AAPL/options?p=AAPL&guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAEPOwasaxXfS0ENDI0K2zYbI1kT7OPT69ESNZ8btuv6ZHKDwG3hPAhSKdMwxGeFUpUH4Hx1-Qo0NfLcmn1Yv6dyVaJkK9NcHci4r4jX7h6j0euuIrfwkZmFWO0oCMcekg50cvJCCtRCYoHRBtI_d2l94UINVM-BKQ9jkNNAVwRU1'
url = 'https://finance.yahoo.com/quote/TSLA/options?p=TSLA'
# html = urllib.request.urlopen(url,context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

###########################################################################3
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

tables = soup.find_all('table')
print("Num Tables: "+ str(len(tables)))
for table in tables:
    df = pd.read_html(str(table))
    # print(table.text)
    display(df[0])

###########################################################################
# dfs = pd.read_html(url,header={'User-Agent': 'Mozilla/5.0'})
# for df in dfs:
#     print(df)

#to do
# Add tables to SQLite database
# Add a column for time to expiration (expiry - current_date)
# write methods to plot volatility of options from database
# Calculate option delta, gamma, other greeks
# Standard deviation of volatility
# Use AI/ML to calculate correlation of greeks with volatility
#

















#








 









