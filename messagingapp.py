
a = True
while a == True:
 b = input("Sign up(1), Log in(2), or quit(3)")
 print    ("♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")


    
 if b == "1":
    name = input("pick a username: ")
    pwd = input("pick a password: ")

    k = open("users.txt","r")
    kline = k.readlines()
    for item in kline:
        if name in item:
            
         print ("sorry, this username is taken")
        
         print ("\n")
         break
        
        else:
        
            open(name+".txt","w")
            
            f = open("users.txt","a")
            f.write(name+" : "+pwd+"\n")
            f.close()
            
            print ("user profile created!")
            
            print ("\n")
            break
    
 if b == "2":
     name = input("enter username: ")
     pwd = input("enter password: ")
     f = open("users.txt","r")
         
     if name not in f.read():
         print ("user not found...")
         print("\n")
         
     else:
         print ("user exists!")
         f = open("users.txt","r")
         line = f.readlines()
         
         
         for item in line:
             if (name in item) and (pwd in item):
                 print("\n")
                 print ("Logging in!")
                 c = input("Send email(1), clear inbox(2) or read inbox(3)? ")
                 if c == "1":
                     user1 = input("Who would you like to send the email to? ")
                     f = open("users.txt","r")
                     if user1 in f.read():
                         print ("this user exists!")
                         msg = input("what message would you like to send? ")
                         msg1 = (msg +"\n")
                         new = open(user1+".txt","a")
                         new.write(msg1)
                         new.close()
                         print("message sent!")
                         print("\n")
                     else:
                         print ("Sorry, this user doesn't exist")
                         print("\n")
                         
                 if c == "2":
                     open(name+".txt","w").close()
                     print ("inbox cleared!")
                     print("\n")

                 if c == "3":
                     f = open(name+".txt","r")
                     print ("♡♡♡Your messages♡♡♡")
                     print("\n")
                     print (f.read())
                     print ("\n")
                     print("♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ")
             elif (name in item) and (pwd not in item):
                 print ("wrong password!")
                 print("\n")
 if b == "3":
     print ("quitting application!")
     print    ("♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
     break
     
         
     
    
    
        
    
