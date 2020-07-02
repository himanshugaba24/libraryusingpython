import Book_Func
from Book_Menu import Book_Menu
from Rack_Menu import Rack_Menu
from Student_Menu import Student_Menu
from Teacher_Menu import Teacher_Menu
from Publisher_Menu import Publisher_Menu
from Transaction_Menu import Transaction_Menu
ch='1' 
def Main_Menu():
    print 40*'\n'
    print 42*" ","- - - - - - - - - - - MAIN MENU - - - - - - - - - - -"
    print 
    print 50*" ","-----------------------------------"
    print 50*" ","!     Menu    ! Key to be Pressed !"
    print 50*" ","-----------------------------------"
    print 50*" ","!     Book    !        '1'        !"
    print 50*" ","!     Rack    !        '2'        !"
    print 50*" ","!    Query    !        '3'        !"
    print 50*" ","!   Student   !        '4'        !"
    print 50*" ","!   Teacher   !        '5'        !"
    print 50*" ","!  Publisher  !        '6'        !"
    print 50*" ","! Transaction !        '7'        !"
    print 50*" ","!     Exit    !        '0'        !"
    print 50*" ","-----------------------------------"
    print
    ch=raw_input("Enter Choice")
    if ch=='1':
        Book_Menu()
    elif ch=='2':
        Rack_Menu()
    elif ch=='3':
        Book_Func.Search()
    elif ch=='4':
        Student_Menu()
    elif ch=='5':
        Teacher_Menu()
    elif ch=='6':
        Publisher_Menu()
    elif ch=='7':
        Transaction_Menu()
    return ch
while ch!='0':
    ch=Main_Menu()
    if ch=='0':
        break  
        
