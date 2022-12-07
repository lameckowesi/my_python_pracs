size = input ("What size of pizza do you want? ")

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25

add_pepperoni = input("Do you want pepperoni? ")

if add_pepperoni == "Y" and size == "S":
    price += 2
elif add_pepperoni == "Y" and size == "M" or size == "L":
    price += 3

extra_cheese = input("Add extra cheese? ")

if extra_cheese == "Y":
    price += 1

print(f"Okay your bill is $ {price}")
