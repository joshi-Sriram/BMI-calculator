print("Welcome to Tip calculator")
bill = int(input("enter your total bill: "))
Tip = int(input("what persentage tip would like to give: "))
persons= int(input("how many members are there to split the bill: "))
amount = (bill + (bill*(Tip/100))) / persons
final_amount = "{:.2f}".format(amount)
print(f"each person should Pay {final_amount} ruppes")
