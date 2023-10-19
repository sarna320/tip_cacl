print("Welcome to tip calcualtor\n")
bill=float(input("What was the bill? $"))
tip=float(input("What procentage tip would you like to give? 10, 12, 15?"))
tip=1.0+tip/100
num_of_people=float(input("How many people to split the bill"))
pay=round((bill*tip)/num_of_people,2)
print(f"Each person should pay: $"+format(pay,".2f"))