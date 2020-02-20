import os
import datetime
import platform
import time
import win32com.client
#import psutil
import win32gui
import win32process
 
""" 
def get_pid():
    pids=psutil.pids()

    for pid in pids:
        pid_info=psutil.Process(pid)
        if pid_info.name()==r"WINWORD.EXE":
            print("WINWORD.EXE PID OK",end=" ")
            print(pid)
            
            return pid
      

def get_hwnds_for_pid (pid):
    def callback (hwnd, hwnds):
        _,found_pid = win32process.GetWindowThreadProcessId (hwnd)
            
        if found_pid == pid:
            print("found_pid is",end=" ")
            print(pid)
            print("ok pid hwnd is  now",end=" ")
            print(hwnd)
            #os.system("pause")
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd):
                print("ok")
                hwnds.append(hwnd)
            else:
                print("false")
             
            return True
    hwnds=[]
    win32gui.EnumWindows (callback,hwnds)
    
    return hwnds



if __name__ == "__main__":
   word_pid=get_pid()
   word_hwnd=get_hwnds_for_pid(word_pid)
   print(word_hwnd[0])
    
   
    
     
  
   
    """


print(os.getcwd())