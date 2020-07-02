import Teacher_Func   
def Teacher_Menu():
    print 40*'\n'
    print 42*" ","- - - - - - - - - - TEACHER  MENU - - - - - - - - - - -"
    print 
    print 50*" ","----------------------------------------"
    print 50*" ","!     Function     ! Key to be Pressed !"
    print 50*" ","----------------------------------------"
    print 50*" ","!   Add Teacher    !        '1'        !"
    print 50*" ","!  Modify Teacher  !        '2'        !"
    print 50*" ","!  Delete Teacher  !        '3'        !"
    print 50*" ","!  Search Teacher  !        '4'        !"
    print 50*" ","! List of Teachers !        '5'        !"
    print 50*" ","!       Exit       !        '0'        !"
    print 50*" ","----------------------------------------"
    ch=raw_input("Enter Choice")
    while ch!='0':
        if ch=='1':
            Teacher_Func.Write()
        elif ch=='2':
            Teacher_Func.Update()
        elif ch=='3':
            Teacher_Func.Delete()
        elif ch=='4':
            n=raw_input("Enter Id - ")
            Teacher_Func.Search_Teacher(n)
        elif ch=='5':
            Teacher_Func.Read()
        else:
            print "Invalid Choice"
        print
        ch=raw_input("Enter choice")
