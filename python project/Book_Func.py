import pickle
import os
class Book():
    def __init__(self):
        self.B_id=0
        self.B_name=''
        self.B_author=''
        self.B_publ=''
        self.B_status=''
        self.B_location=''
    def getInfo(self):
        self.B_name=raw_input("Enter book Name-") 
        self.B_author=raw_input("Enter book Author-")
        self.B_publ=raw_input("Enter book Publisher-")
        self.B_status=raw_input("Book issued or not(Yes or No)-")
        self.B_location=raw_input("Enter book Location-")
    def display(self):
        print "Book details are:-"
        print "Id- ",self.B_id
        print "Name- ",self.B_name
        print "Author- ",self.B_author
        print "Publisher- ",self.B_publ
def Write():
    try:
        f=file("Book Master.dat","rb")
        b=Book()
        while True:
            b=pickle.load(f)
    except IOError:
        Add(100)
    except EOFError:
        Add(b.B_id)
def Add(x):
    f=file("Book Master.dat","ab")
    n=input("Enter the no of Book to add -")
    x=x+11
    i=0
    b=Book()
    while i<n:
        b.getInfo()
        b.B_id=x
        pickle.dump(b,f)
        upd_rack(b.B_location,1)
        print
        i+=1
        x+=11
    f.close()
def Read():
    try:
        f=file("Book Master.dat","rb")
        b=Book()
        i=1
        print "S.No.","Book Id"," "*9,"Books Name",28*" ","Author",18*" ","Publisher",16*" ","Rack Name",4*" ","status"
        while True:
            j=str(i)
            b=pickle.load(f)
            print i,"."," "*(4-len(j)),b.B_id,4*" ",b.B_name,(43-len(b.B_name))*" ",b.B_author,(24-len(b.B_author))*" ",b.B_publ,(27-len(b.B_publ))*" ",b.B_location,(15-len(b.B_location))*" ",b.B_status
            i+=1
    except EOFError:
        f.close()
def Search_Book():
    try:
        f=open("Book Master.dat","rb")
        n=input("Enter Book Id - ")
        b=Book()
        while True:
           b=pickle.load(f)
           if b.B_id==n:
               b.display()
               break
        f.close()
    except:
        print "Invalid Id"
        f.close()
def Search():
   try:
      print
      f=open("Book Master.dat","rb")
      n=raw_input("Enter Book to Search - ")
      p=raw_input("Enter  book publisher - ")
      flag=0
      while True:
         b=pickle.load(f)
         if b.B_name==n and b.B_status=='No'and b.B_publ==p:
            print
            print " ' Book Available ' "
            print
            b.display()
            break
         elif b.B_name==n and b.B_status=='Yes'and b.B_publ==p:
            print " ' Book already Issued By someone '"
            flag=1
            break
      f.close()
      print
      ch=raw_input("Enter choice('0' to Exit and '1' to Search a Book) - ")
      if ch=='1':
         Search()
   except EOFError:
       if flag==0:
           print "Invalid Id"
       else:
            pass
def Update():
    try:
        f=open("Book Master.dat","rb")
        f1=open("temp.dat","wb")
        Id=input("Enter id - ")
        b=Book()
        flag=0
        while True:
            b=pickle.load(f)
            if b.B_id==Id:
                b.B_publ=raw_input("Enter new publisher - ")
                flag=1
            pickle.dump(b,f1)
    except EOFError:
        if flag==0:
            print "Invalid Id"
        f.close()
        f1.close()
        os.remove("Book Master.dat")
        os.rename("temp.dat","Book Master.dat")
    except:
        f.close()
        f1.close()
def Delete():
    try:
        f=open("Book Master.dat","rb")
        f1=open("temp.dat","wb")
        id=input("Enter id - ")
        flag=0
        b=Book()
        while True:
            b=pickle.load(f)
            if b.B_id==id:
                upd_rack(b.B_location,-1)
                flag=1
            else:
                pickle.dump(b,f1)
    except EOFError:
        if flag==0:
            print "Invalid Id"
        f.close()
        f1.close()
        os.remove("Book Master.dat")
        os.rename("temp.dat","Book Master.dat")
    except IOError:
        f.close()
    except:
        f.close()       
        f1.close()
def upd_rack(n,m):
    try:
        f2=file("Rack Master.dat","rb")
        f3=file("temp1.dat","wb")
        r=Rack()
        while True:
            r=pickle.load(f1)
            if r.r_name==n and m==1:
                r.r_qty+=1
            elif r.r_name==n and m==-1:
                r.r_qty-=1
            pickle.dump(r,f2)
    except EOFError:
        f2.close()
        f3.close()
        os.remove("Rack Master.dat")
        os.rename("temp.dat","Rack Master.dat")
    except:
        pass












            
        
