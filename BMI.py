height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height /100)**2
print("your BMI is", BMI)


if BMI <=18.9:
    print("You are underweight")
elif BMI <=24.9:
    print("You are healthy")
elif BMI <=29.9:
    print("You are overweight")
elif BMI <=34.9:
    print("You are severely overweight")
else:
    print("You are obese")