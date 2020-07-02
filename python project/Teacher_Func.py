import pickle
import os
class Teacher:
    def __init__(self):
        self.t_id=''
        self.t_name=''
        self.t_status=''
    def getData(self):
        self.t_id=raw_input("Enter Teacher Id - ")
        self.t_name=raw_input("Enter Teacher Name - ") 
        self.t_status=raw_input("Book issued or not(Yes or No) - ")
    def display(self):
        print "Teacher details are:-"
        print "Id - ",self.t_id
        print "Name - ",self.t_name
        print "Present status - ",self.t_status
def Write():
    f=file("Teacher Master.dat","ab")
    n=input("Enter the no of record to write - ")
    i=0
    t=Teacher()
    while i<n:
        t.getData()
        pickle.dump(t,f)
        print
        i+=1
    f.close()
def Read():
    try:
        f=file("Teacher Master.dat","rb")
        t=Teacher()
        i=1
        print "S.No.","Teacher_Id"," ","Teacher_Name","Status"
        while True:
            j=str(i)
            t=pickle.load(f)
            print i,".",(3-len(j))*" ",t.t_id,(12-len(t.t_id))*" ",t.t_name,(12-len(t.t_name))*" ",t.t_status
            i+=1
    except EOFError:
        f.close()
def Search_Teacher(Id):
    try:
        f=file("Teacher Master.dat","rb")
        t=Teacher()
        while True:
            t=pickle.load(f)
            if t.t_id==Id:
                t.display()
                break
        f.close()    
    except EOFError:
        print "Invalid Id"
        f.close()
def Search(Id):
    try:
        f=file("Teacher Master.dat","rb")
        t=Teacher()
        while True:
            t=pickle.load(f)
            if t.t_id==Id:
                f.close()
                return 'True'
    except EOFError:
        f.close()
def Update():
    try:
        t=Teacher()
        Id=raw_input("Enter id - ")
        a=Search(Id)
        if a=='True':
            f=open("Teacher Master.dat","rb")
            f1=open("temp.dat","wb")
            while True:
                t=pickle.load(f)
                if t.t_id==Id:
                    t.t_id=raw_input("Enter new id - ")
                pickle.dump(t,f1)
        else:
            print "Invalid Id"
    except EOFError:
        f.close()
        f1.close()
        os.remove("Teacher Master.dat")
        os.rename("temp.dat","Teacher Master.dat")
    except IOError:
        print "Some Error"
        pass
def Delete():
    try:
       f=open("Teacher Master.dat","rb")
       f1=open("temp.dat","wb")
       id=raw_input("Enter id - ")
       t=Teacher()
       while True:
           t=pickle.load(f)
           if t.t_id!=id:
                pickle.dump(t,f1)
    except EOFError:
        f.close()
        f1.close()
        os.remove("Teacher Master.dat")
        os.rename("temp.dat","Teacher Master.dat")
