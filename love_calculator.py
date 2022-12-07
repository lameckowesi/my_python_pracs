your_name = input("What is your first name? ")
spouse_name = input("What is your spouse's first name? ")
added_names = your_name + spouse_name

combined_name = added_names.lower()
true_score= int(combined_name.count("t") + combined_name.count ("r") + combined_name.count("u") + combined_name.count("e") )
love_score = int(combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e"))

compatibility_score = int(str(true_score) + str(love_score))

if compatibility_score >=40 and compatibility_score<=50:
    print(f"Your score is {compatibility_score}, you are alright together")
elif compatibility_score <10 or compatibility_score >90:
    print(f"Your score is {compatibility_score},you go together like coke and mentos!")
else:
    print (f"Your love compatibility score is {compatibility_score}")