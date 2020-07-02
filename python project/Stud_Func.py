import pickle
import os
class Student:
    def __init__(self):
        self.s_id=''
        self.s_name=''
        self.s_class=0
        self.s_status=''
    def getData(self):
        self.s_id=raw_input("Enter student Id- ")
        self.s_name=raw_input("Enter student Name-") 
        self.s_class=input("Enter student class-")
        self.s_status=raw_input("Book issued or not(Yes or No)-")
    def display(self):
        print "Student details are:-"
        print "Id-",self.s_id
        print "Name-",self.s_name
        print "Class-",self.s_class
        print "Present status-",self.s_status
def Write():
    f=file("Student Master.dat","ab")
    n=input("Enter the no of record to write-")
    i=0
    s=Student()
    while i<n:
        s.getData()
        pickle.dump(s,f)
        print
        i+=1
    f.close()
def Read():
    try:
        f=file("Student Master.dat","rb")
        s=Student()
        i=1
        print "S.No.","Student_Id","Student_Name","Class","Status"
        while True:
            j=str(i)
            s=pickle.load(f)
            print i,".",(3-len(j))*" ",s.s_id," ",s.s_name,(12-len(s.s_name))*" ",s.s_class,(4-len(str(s.s_class)))*" ",s.s_status
            i+=1
    except EOFError:
        f.close()
def Search_student(Id):
    try:
        f=file("Student Master.dat","rb")
        s=Student()
        while True:
            s=pickle.load(f)
            if s.s_id==Id:
                s.display()
                break
        f.close()    
    except EOFError:
        print "Invalid Id"
        f.close()
def Search(Id):
    try:
        f=file("Student Master.dat","rb")
        s=Student()
        while True:
            s=pickle.load(f)
            if s.s_id==Id:
                f.close()
                return 'True'
    except EOFError:
        f.close()
def Update():
    try:
        s=Student()
        Id=raw_input("Enter id - ")
        a=Search(Id)
        if a=='True':
            f=open("Student Master.dat","rb")
            f1=open("temp.dat","wb")
            while True:
                s=pickle.load(f)
                if s.s_id==Id:
                    s.s_class=input("Enter new class - ")
                pickle.dump(s,f1)
        else:
            print "Invalid Id"
    except EOFError:
        f.close()
        f1.close()
        os.remove("Student Master.dat")
        os.rename("temp.dat","Student Master.dat")
    except IOError:
        print "Some Error"
        pass
def Delete():
    try:
       f=open("Student Master.dat","rb")
       f1=open("temp.dat","wb")
       id=raw_input("Enter id - ")
       s=Student()
       while True:
           s=pickle.load(f)
           if s.s_id!=id:
                pickle.dump(s,f1)
    except EOFError:
        f.close()
        f1.close()
        os.remove("Student Master.dat")
        os.rename("temp.dat","Student Master.dat")

