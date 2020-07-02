import pickle
import os
class Publisher:
      def __init__(self):
            self.p_id=0
            self.p_name=" "
            self.p_addr=" "
            self.p_no=0
      def inputdata(self):
            self.p_name=raw_input("Enter Publisher name - ")
            self.p_add=raw_input("Enter Publisher Address - ")
            self.p_no=input("Enter Publisher Phone no. - ")
      def display(self):
            print "Details of Publisher are:-"
            print "Id - ",self.p_id
            print "Name - ",self.p_name
            print "Address - ",self.p_add
            print "Phone no. - ",self.p_no
def Write():
    try:
        f=file("Publisher Master.dat","rb")
        publ=Publisher()
        while True:
            publ=pickle.load(f)
    except IOError:
        Add(1234)
    except EOFError:
        Add(publ.p_id)   
def Add(x):
    f=file("Publisher Master.dat","ab")
    n=input("Enter the no of Publishers to add - ")
    x=x+25
    i=0
    publ=Publisher()
    while i<n:
        publ.inputdata()
        publ.p_id=x
        pickle.dump(publ,f)
        print
        i+=1
        x+=25
def Read():
    try:
        f=file("Publisher Master.dat","rb")
        publ=Publisher()
        i=1
        print "S.No.","Publisher Id",4*" ","Publisher_Name",17*" ","Address",40*" ","Phone No"
        while True:
            j=str(i)
            publ=pickle.load(f)
            print i,"."," "*(6-len(j)),publ.p_id,4*" ",publ.p_name,(27-len(publ.p_name))*" ",publ.p_add,(55-len(publ.p_add))*" ",publ.p_no
            i+=1
    except EOFError:
        f.close()
def Search():
    try:
        f=open("Publisher Master.dat","rb")
        Id=input("Enter id - ")
        publ=Publisher()
        while True:
            publ=pickle.load(f)
            if publ.p_id==Id:
                    publ.display()
                    break
        f.close()
    except:
        print "Invalid Publ. Id"
        f.close()
def Update():
    try:
        f=open("Publisher Master.dat","rb")
        f1=open("temp.dat","wb")
        id=input("Enter id - ")
        publ=Publisher()
        flag=0
        while True:
            publ=pickle.load(f)
            if publ.p_id==id:
                publ.p_add=raw_input("Enter new address - ")
                flag=1
            pickle.dump(publ,f1)
    except EOFError:
        if flag==0:
            print "Invalid Publ. Id"
        f.close()
        f1.close()
        os.remove("Publisher Master.dat")
        os.rename("temp.dat","Publisher Master.dat")
    except:
        f.close()
        f1.close()
def Delete():
    try:
        f=open("Publisher Master.dat","rb")
        f1=open("temp.dat","wb")
        Id=input("Enter id - ")
        publ=Publisher()
        flag=0
        while True:
            publ=pickle.load(f)
            if publ.p_id==Id:
                flag=1
            else:
                pickle.dump(publ,f1)
    except EOFError:
        if flag==0:
            print "Invalid Publ. Id" 
        f.close()
        f1.close()
        os.remove("Publisher Master.dat")
        os.rename("temp.dat","Publisher Master.dat")
    except:
        f.close()
        f1.close()

