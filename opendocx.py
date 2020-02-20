import os
import sys
from win32com.client import Dispatch
import pywintypes
from comtypes.client import CreateObject
import comtypes


 
app = Dispatch('Word.Application')
 
doc = app.Documents.Open(r"D://pythontest//1.docx")

app.visible=True


  

 
""" passw=[]
dic = open("pass1.txt","r")
data=dic.readline().strip('\n')

while len(data)!=0:
    passw.append(data)
    data=dic.readline().strip('\n')
dic.close()




word=win32com.client.Dispatch("Word.Application")
word.visible = True
 


for i in passw:
    try:
        print(i)
        doc = word.Documents.Open(r"D://pythontest//1.docx",PasswordDocument=i)           
    except pywintypes.com_error:
        print(i)
        continue
    print("succcccceesss"+i) """