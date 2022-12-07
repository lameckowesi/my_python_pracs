weight = input("Enter your weight in Kg ")

height = input ("Enter your height in metres ")

recorded_weight = float(weight)
recorded_height = float(height)

BMI = (recorded_weight)/(recorded_height**2)

reported_BMI = int(BMI)


print (f"your BMI is {reported_BMI}")

if reported_BMI < 18.5:
    print ("You are underweight")
elif reported_BMI >= 18.5 and reported_BMI < 25:
    print("You have normal weight")
elif reported_BMI >=25 and reported_BMI < 30:
    print ("you are overweight")
elif reported_BMI >= 30 and reported_BMI <35:
    print ("you are obese")
else:
    print("you are clinically obese")