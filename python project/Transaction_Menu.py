import IssueBook
def Transaction_Menu():
   print '\n'*40
   print 42*" ","- - - - - - - - - - - TRANSACTION MENU - - - - - - - - - - -"
   print 
   print 50*" ","----------------------------------------"
   print 50*" ","! Transaction Menu ! Key to be Pressed !"
   print 50*" ","----------------------------------------"
   print 50*" ","!  To Issue a Book !        '1'        !"
   print 50*" ","! To Return a Book !        '2'        !"
   print 50*" ","!       Exit       !        '0'        !"
   print 50*" ","----------------------------------------"
   ch=raw_input("Enter Choice")
   while ch!='0':
      if ch=='1':
           IssueBook.Issue()
      elif ch=='2':
           IssueBook.Return()
      else:
           print "Invalid Choice"
      print
      ch=raw_input("Enter Choice")
