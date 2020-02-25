import os
import sys
from win32com.client import Dispatch
from win32com.client import DispatchEx

word = Dispatch('Word.Application')

word.Documents.Open(FileName=u'D://pythontest//a.docx',
                     
                   
                    PasswordDocument=12332122,
                    
                   
                   
                    
                     
                    
                    
                    )


""" 
passw = []
dic = open("pass1.txt", "r")
data = dic.readline().strip('\n')

while len(data) != 0:
    passw.append(data)
    data = dic.readline().strip('\n')


dic.close()

wps1 = Dispatch('word.Application')

wps1.Visible = True
wps1.DisplayAlerts = 0

for i in passw:

    try:
        d = wps1.Documents.Open(r'D://pythontest//a.docx', UpdateLinks=False,
                                ReadOnly=False, Format=None,  PasswordDocument=i, WriteResPassword=)
    except pywintypes.com_error:

        print(i)
        continue
    print("succcccceesss"+i)
 """
