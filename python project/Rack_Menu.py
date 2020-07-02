import Rack_Func
def Rack_Menu():
    print 40*'\n'
    print 40*" ","- - - - - - - - - - - Rack  MENU - - - - - - - - - - -"
    print 
    print 50*" ","-------------------------------------"
    print 50*" ","!    Function   ! Key to be Pressed !"
    print 50*" ","-------------------------------------"
    print 50*" ","!    Add Rack   !        '1'        !"
    print 50*" ","!  Modify Rack  !        '2'        !"
    print 50*" ","!  Delete Rack  !        '3'        !"
    print 50*" ","!  Search Rack  !        '4'        !"
    print 50*" ","! List of Racks !        '5'        !"
    print 50*" ","!     Exit      !        '0'        !"
    print 50*" ","-------------------------------------"
    ch=raw_input("Enter Choice")
    while ch!='0':
        if ch=='1':
            Rack_Func.Write()
        elif ch=='2':
            Rack_Func.Update()
        elif ch=='3':
            Rack_Func.Delete()
        elif ch=='4':
            Rack_Func.Search()
        elif ch=='5':
            Rack_Func.Read()
        else:
            print "Invalid Choice"
        print
        ch=raw_input("Enter Choice")
