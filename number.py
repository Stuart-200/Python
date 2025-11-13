
number =int(input("Enter a three-digit number: "))

num1 = number // 100
num2 = (number // 10) % 10
num3 = number % 10

sum_of_num= num1**3 + num2**3 + num3**3
print("%d³ + %d³ + %d³ = %d" % (num1, num2, num3, sum_of_num))



is_armstrong = (sum_of_num == number)

if sum_of_num == number:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")

