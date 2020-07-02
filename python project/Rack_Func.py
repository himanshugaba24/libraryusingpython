import pickle
import os
class Rack:
    def __init__(self):
        self.r_name=" "
        self.r_qty=0
    def getdata(self):
        self.r_name=raw_input("Enter Rack Name - ")
        self.r_qty=input("Enter no. of Books - ")
    def display(self):
        print "Rack Details are:- "
        print "Name - ",self.r_name
        print "No. of Books - ",self.r_qty
def Write():
    f=open("Rack Master.dat","ab")
    n=input("Enter no of Racks to add - ")
    i=0
    R=Rack()
    while i<n:
        R.getdata()
        pickle.dump(R,f)
        print
        i+=1
    f.close()
def Read():
    try:
        f=open("Rack Master.dat","rb")
        R=Rack()
        print "S.No."," Rack_Name",3*" ","No. of Books"
        i=1
        while True:
            j=str(i)
            R=pickle.load(f)
            print i,".",(3-len(j))*" ",R.r_name,(17-len(R.r_name))*" ",R.r_qty
            i+=1
    except EOFError:
        f.close()
def Search():
    try:
        f=open("Rack Master.dat","rb")
        n=raw_input("Enter Rack Name - ")
        R=Rack()
        while True:
           R=pickle.load(f)
           if R.r_name==n:
               R.display()
               break
        f.close()
    except:
        print "Invalid Id"
        f.close()
def Update():
    try:
       f=open("Rack Master.dat","rb")
       f1=open("temp.dat","wb")
       f2=0
       n=raw_input("Enter Rack name - ")
       R=Rack()
       while True:
           R=pickle.load(f)
           if R.r_name==n:
               f2=1
               R.r_qty=input("Enter new quantity - ")
           pickle.dump(R,f1)
    except EOFError:
        if f2==0:
            print "Invalid Rack Name"
        f.close()
        f1.close()
        os.remove("Rack Master.dat")
        os.rename("temp.dat","Rack Master.dat")
    except:
        f.close()
        f1.close()
def Delete():
    try:
       f=open("Rack Master.dat","rb")
       f1=open("temp.dat","wb")
       f2=0
       n=raw_input("Enter Rack to Delete - ")
       R=Rack()
       while True:
           R=pickle.load(f)
           if R.r_name!=n:
               f2=1
               pickle.dump(R,f1)
    except EOFError:
        if f2==0:
            print "Invalid Rack Name"
        f.close()
        f1.close()
        os.remove("Rack Master.dat")
        os.rename("temp.dat","Rack Master.dat")
    except:
        f.close()
        f1.close()

