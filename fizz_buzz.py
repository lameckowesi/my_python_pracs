for kid_position in range (1,101):
    if kid_position % 3 == 0 and kid_position % 5 ==0:
        shout = "fizzbuzz"
    elif kid_position % 3 ==0:
        shout = "fizz"
    elif kid_position % 5 == 0:
        shout = "buzz"
    
    else:
        shout = kid_position
    print (shout)