import Book_Func
def Book_Menu():
    print 40*'\n'
    print 42*" ","- - - - - - - - - - - BOOK MENU - - - - - - - - - - -"
    print 
    print 50*" ","-------------------------------------"
    print 50*" ","!    Function   ! Key to be Pressed !"
    print 50*" ","-------------------------------------"
    print 50*" ","!   Add Book    !        '1'        !"
    print 50*" ","!  Modify Book  !        '2'        !"
    print 50*" ","!  Delete Book  !        '3'        !"
    print 50*" ","!  Search Book  !        '4'        !"
    print 50*" ","! List of Books !        '5'        !"
    print 50*" ","!      Exit     !        '0'        !"
    print 50*" ","-------------------------------------"
    ch=raw_input("Enter Choice")
    while ch!='0':
        if ch=='1':
            Book_Func.Write()
        elif ch=='2':
            Book_Func.Update()
        elif ch=='3':
            Book_Func.Delete()
        elif ch=='4':
            Book_Func.Search_Book()
        elif ch=='5':
            Book_Func.Read()
        else:
            print "Invalid Choice"
        print
        ch=raw_input("Enter choice")
