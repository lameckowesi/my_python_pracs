import random

# Storing friends names in a variable

buddies = input("Enter buddy names separated by comma and space: ")

# splitting the names into a list
buddy_names = buddies.split(", ")
print(buddy_names)

# Randomly assigning any name from the list to pay bill
number_of_names = len(buddy_names)
random_position = random.randint(0, number_of_names - 1)
bill_payer = buddy_names[random_position]

# using the random choice function to assign bill payer

bill_payer = random.choice(buddy_names) #A shorter code for the random assigning logic

print(f"The one paying our bill today is {bill_payer}")