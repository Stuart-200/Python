def checkifSame(number1,number2):
    if number1 ^ number2 !=0:
       print("The numbers are not same")
    else:
        print("The numbers are same")
    
    
number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))


checkifSame(number1,number2)