print("Welcome to Tip calculator")
bill = int(input("enter your total bill: "))
Tip = int(input("what persentage tip would like to give: "))
persons= int(input("how many members are there to split the bill: "))
amount = (bill + (bill*(Tip/100))) // persons
print(amount) 