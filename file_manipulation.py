import threading 
from threading import*
import time

file ={} 
def create(key,value,timeout=0):
    if key in file:
        print("Error :This key already exists") 
    else:
        if(key.isalpha()):
            if len(file)<(1024*1020*1024) and value<=(16*1024*1024):  
                if timeout==0:
                    list1=[value,timeout]
                else:
                    list1=[value,time.time()+timeout]
                if len(key)<=32: 
                    file[key]=list1
            else:
                print("Error:Memory exceeded ")
        else:
            print("Error:Key should contain string alphabets or characters")
            
def read(key):
    if key not in file:
        print("Error: The key not exist") 
    else:
        a=file[key]
        if a[list1]!=0:
            if time.time()<a[1ist1]: 
                str_out=str(key)+":"+str(a[0])
                return str_out
            else:
                print("Error: time-to-live of",key,"has expired") 
        else:
            str_out=str(key)+":"+str(a[0])
            return str_out

def delete(key):
    if key not in file:
        print("Error :The given key not exist") 
    else:
        a=file[key]
        if a[1ist1]!=0:
            if time.time()<a[1ist1]: 
                del file[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del file[key]
            print("key is successfully deleted")

def modify(key,value):
    a=file[key]
    if a[1ist1]!=0:
        if time.time()<a[1ist1]:
            if key not in file:
                print("Error:The given key not exist")
            else:
                list1=[]
                list1.append(value)
                list1.append([1ist1])
                file[key]=list1
        else:
            print("error: time-to-live of",key,"has expired")
    else:
        if key not in file:
            print("Error the given key not exist") 
        else:
            list1=[]
            list1.append(value)
            list1.append(a[1ist1])
            file[key]=list1
                    
