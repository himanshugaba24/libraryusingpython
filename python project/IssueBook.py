import pickle
import os
from Teacher_Func import Teacher #phle wala module and second is a function
from Stud_Func import Student
from Book_Func import Book
from Rack_Func import Rack
def Upd_R(n,s):
    try:
        f3=open("Rack Master.dat","rb")
        f2=open("temp1.dat","wb")
        r=Rack()
        while True:
            r=pickle.load(f3)
            if r.r_name==n and s=="Yes":
                r.r_qty=r.r_qty-1
            elif r.r_name==n and s=="No":
                r.r_qty=r.r_qty+1
            pickle.dump(r,f2)
    except EOFError:
        f3.close()
        f2.close()
        os.remove("Rack Master.dat")
        os.rename("temp1.dat","Rack Master.dat")
def Upd_T(n,Id=0):
    try:
        f2=open("Teacher Master.dat","rb")
        f3=open("temp1.dat","wb")
        t=Teacher()
        while True:
            t=pickle.load(f2)
            if t.t_id==n and Id==0:
                t.t_status="No"
            elif t.t_id==n and Id!=0:
                t.t_status=Id
            pickle.dump(t,f3)
    except EOFError:
        f2.close()
        f3.close()
        os.remove("Teacher Master.dat")
        os.rename("temp1.dat","Teacher Master.dat")
def Upd_S(n,Id=0):
    try:
        f2=open("Student Master.dat","rb")
        f3=open("temp1.dat","wb")
        s=Student()
        flag=0
        while True:
            s=pickle.load(f2)
            if s.s_id==n and Id==0:
                s.s_status="No"
                flag=1
            elif s.s_id==n and Id!=0:
                s.s_status=Id
                flag=1
            pickle.dump(s,f3)
    except EOFError:
        f2.close()
        f3.close()
        os.remove("Student Master.dat")
        os.rename("temp1.dat","Student Master.dat")
    finally:
        if flag==0:
            Upd_T(n)
def Find_T(n):
    try:
        f2=open("Teacher Master.dat","rb")
        t=Teacher()
        while True:
            t=pickle.load(f2)
            if t.t_id==n and t.t_status=='No':
                f2.close()
                return 'True'
    except:
        f2.close()
def Find_S(n):
    try:
        f2=open("Student Master.dat","rb")
        s=Student()
        while True:
            s=pickle.load(f2)
            if s.s_id==n and s.s_status=='No':
                f2.close()
                return 'True'
    except:
        f2.close()
def Find_B(m):
    try:
        f2=file("Book Master.dat","rb")
        b=Book()
        flag=0
        while True:
            b=pickle.load(f2)
            if b.B_id==m and b.B_status=='No':
                f2.close()
                print " 'Book Found' "
                c=raw_input("Dou you want to Issue this Book(Yes or No) - ")
                if c=='Yes':
                    return 'True'
    except:
        f2.close()
        print "Some error"
def Issue():
    try:
        Bid=input("Enter the book id you want to issue - ")
        Sid=raw_input("Enter your id - ")
        if Find_S(Sid)=='True' and Find_B(Bid)=='True':
            f=open("Book Master.dat","rb")
            f1=open("temp.dat","wb")
            b=Book()
            while True:
                b=pickle.load(f)
                if b.B_id==Bid and b.B_status=="No":
                    b.B_status="Yes"
                    Upd_S(Sid,Bid)
                    Upd_R(b.B_location,b.B_status)
                    print " 'Book Issued '"
                elif b.B_id==Bid and b.B_status!='No':
                    print "Book already Issued"
                pickle.dump(b,f1)
        elif Find_T(Sid)=='True' and Find_B(Bid)=='True':
            f=open("Book Master.dat","rb")
            f1=open("temp.dat","wb")
            b=Book()
            while True:
                b=pickle.load(f)
                if b.B_id==Bid and b.B_status=="No":
                    b.B_status="Yes"
                    Upd_T(Sid,Bid)
                    Upd_R(b.B_location,b.B_status)
                    print " 'Book Issued '"
                elif b.B_id==Bid and b.B_status!='No':
                    print "Book already Issued"
                pickle.dump(b,f1)
        else:
            raise IOError
    except IOError:
       print "sorry"
       
    except EOFError:
        f.close()
        f1.close()
        os.remove("Book Master.dat")
        os.rename("temp.dat","Book Master.dat")
    finally:
        f=open("Issue_Book.txt","a")
        f.write(Sid+"~"+str(Bid)+'\n')
        f.close()  
def Return():
    try:
        f=open("Book Master.dat","rb")
        f1=open("temp.dat","wb")
        Bid=input("Enter Book Id - ")
        Sid=raw_input("Enter your Id - ")
        b=Book()
        while True:
            b=pickle.load(f)
            if b.B_id==Bid and b.B_status=="Yes":
                b.B_status="No"
                Upd_S(Sid)
                Upd_R(b.B_location,b.B_status)
            pickle.dump(b,f1)
    except IOError:
        f.close()
        f1.close()
        os.remove("temp.dat")
    except EOFError:
        f.close()
        f1.close()
        os.remove("Book Master.dat")
        os.rename("temp.dat","Book Master.dat")
    finally:
        f=open("Issue_Book.txt")
        f1=open("temp.txt","w")
        rec=" "
        while rec:
            rec=f.readline()
            l=rec.split("~")
            if l[0]==Sid:
                pass
            else:
                f1.write(rec)
        f.close()
        f1.close()
        os.remove("Issue_Book.txt")
        os.rename("temp.txt","Issue_Book.txt")
        print " 'Book Returned' "
        
