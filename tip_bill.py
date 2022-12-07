bill = int(input("Enter total bill "))

no_of_people = int(input("How many are you? "))

tip = int(input("Enter tip percentage "))

tip_percentage = float(tip/100)

total_tip = bill * tip_percentage

total_bill = bill + total_tip

personal_payable = total_bill / no_of_people

print(f"Your bill share is {personal_payable}, Thank you for visiting!")
