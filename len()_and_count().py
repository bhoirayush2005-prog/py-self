#math 
password = "2845233"
print(len(password))   #len() shows the lenght of object

if len(password) < 8:   
    print("your password is too short")


#count() method       
text = """hi my name is ayush
and i love to ride bikes 
also ayush loves swimming and all
also ayush loves listening music and stuff"""
A = text.count("ayush")
print("in text ayush was typed",A," times")   # ayush used 3 times
#also count() is case sensitive 


B = "342483275834053485348576384657023453485384758345638405834"
print(B.count("5"))