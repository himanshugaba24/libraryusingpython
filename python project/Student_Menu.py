import Stud_Func   
def Student_Menu():
    print 40*'\n'
    print 42*" ","- - - - - - - - - - STUDENT  MENU - - - - - - - - - - -"
    print 
    print 50*" ","----------------------------------------"
    print 50*" ","!     Function     ! Key to be Pressed !"
    print 50*" ","----------------------------------------"
    print 50*" ","!   Add Student    !        '1'        !"
    print 50*" ","!  Modify Student  !        '2'        !"
    print 50*" ","!  Delete Student  !        '3'        !"
    print 50*" ","!  Search Student  !        '4'        !"
    print 50*" ","! List of Students !        '5'        !"
    print 50*" ","!       Exit       !        '0'        !"
    print 50*" ","----------------------------------------"
    ch=raw_input("Enter Choice")
    while ch!='0':
        if ch=='1':
            Stud_Func.Write()
        elif ch=='2':
            Stud_Func.Update()
        elif ch=='3':
            Stud_Func.Delete()
        elif ch=='4':
            n=raw_input("Enter Id - ")
            Stud_Func.Search_student(n)
        elif ch=='5':
            Stud_Func.Read()
        else:
            print "Invalid Choice"
        print
        ch=raw_input("Enter choice")
