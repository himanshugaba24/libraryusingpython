import Publ_Func
def Publisher_Menu():
      print 40*'\n'
      print 42*" "," - - - - - - - - - - - PUBLISHER  MENU - - - - - - - - - - "
      print 
      print 50*" ","------------------------------------------"
      print 50*" ","!       Function     ! Key to be Pressed !"
      print 50*" ","------------------------------------------"
      print 50*" ","!    Add Publisher   !        '1'        !"
      print 50*" ","!  Modify Publisher  !        '2'        !"
      print 50*" ","!  Delete Publisher  !        '3'        !"
      print 50*" ","!  Search Publisher  !        '4'        !"
      print 50*" ","! List of Publishers !        '5'        !"
      print 50*" ","!       Exit         !        '0'        !"
      print 50*" ","------------------------------------------"
      ch=raw_input("Enter Choice")
      while ch!='0':
            if ch=='1':
                  Publ_Func.Write()
            elif ch=='2':
                  Publ_Func.Update()
            elif ch=='3':
                  Publ_Func.Delete()
            elif ch=='4':
                  Publ_Func.Search()
            elif ch=='5':
                  Publ_Func.Read()
            else:
                  print "Invalid Choice"
            print
            ch=raw_input("Enter Choice")
