number = int(input("Enter a number: "))

digits = len(str(number))
result_number = 0

temp = number 

while temp > 0:
    digit = temp % 10
    result_number = result_number + digit ** digits
    temp = temp // 10
    
if number ==  result_number:
    print(number, "Is an Armstrong number")
else:
    print(number, "Is not an Armstrong number")