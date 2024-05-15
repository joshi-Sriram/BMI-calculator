print("welcome to pizza hut:) ")
size= input("what size of pizza do you want small(S)=15rs or medium(M)=20rs and large(L)=25: ")
bill = 0
if size == "S":
    bill +=15
    pepperoni = input("do you like to add pepperoni for small pizza  type yes(Y)=2rs or No(N)=0rs: ")
    if pepperoni == "Y":
        bill +=2 
    else:
        pass
elif size == "M":
    bill +=20
    pepperoni = input("do you like to add pepperoni for medium pizza  type yes(Y)=3rs or No(N)=0rs: ")
    if pepperoni == "Y":
        bill +=3
    else:
        pass
elif size == "L":
    bill +=25
    pepperoni = input("do you like to add pepperoni for large pizza  type yes(Y)=3rs or No(N)=0rs: ")
    if pepperoni == "Y":
        bill +=3
    else:
        pass
cheese = input("do you need cheese for any pizza its just add 1rs to your bill yes(Y) or no(N): ")
if cheese == "Y":
    bill  +=1
  
else:
    print("please choose which size of pizza do u want!")
print(f"you are our lovely coustomer we added some extra love to it and your bill is {bill}rs thank you hope you love it:)")
    