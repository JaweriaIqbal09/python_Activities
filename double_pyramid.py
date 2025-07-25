while True:
    height=(int(input("Enter Any Value from 1 to 8 (inclusive) : ")))
    if (height<1 or height>8):
        print("Please Enter The Valid Number !")
    else:
        break
dot=height
for i in range (1,(1+height),1):
    dot -=1 
    print((dot)*"."+ i*"#", end =" ")
    if i==1:
        print("====",end=" ")
    else:
        print("....",end=" ")
    print(i*"#"+(dot)*".")    
       