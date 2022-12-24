import random

words = ["lameck", "val", "sule"]

chosen_word = random.choice(words)

print (f"Solution is: {chosen_word}")

end_of_game = False
def guessing():
    display = []
    for letter in chosen_word:
        display += "_"
    # print (display) 

    # for letter in chosen_word:
    #     if guess == letter:
    #         display += guess

    # print(display)

    guess = input ("Enter a letter: ").lower()

    # display = []
    for position in range (len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] += letter

    print(display)

while not end_of_game:
    guessing()

if "_" not in chosen_word:
    end_of_game = True    

    print("You Win!")
