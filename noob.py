#!/usr/bin/env python2

import os
import smtplib
import getpass

w = '\033[0m'
g = '\033[32m'
c = '\033[1;36;40m'

os.system("clear")

# From adrress & To address
fromaddress = raw_input("\033[1;97mFrom address: ")
toaddress = raw_input("\033[1;97mTo address: ")

os.system("clear")
print  """
\033[1;97mTHIS IS FOR EDUCATIONAL PURPOSES ONLY
# Gmail Login
username = raw_input("\033[1;93mYour email: ")
password = getpass.getpass("\033[1;93mPassword: ")

# message
message = raw_input("\033[1;97mYour message: ")

# Creating a connection
server =smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

# for loop to send multiple spam
total = input("Total spam: ")
print c+"\n[*]"+w+" Running . . ."+w
for i in range (total):
  server.sendmail(fromaddress,toaddress,message)
  print g+"[*]"+w+" mail sent"
  
server.quit()
