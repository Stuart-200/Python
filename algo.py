def multiply_1_iteration(a,b):
    return a * b

def multiply_n_iterations(a,b):
    sum = 0
    for a in range(b):
        sum+= a
    return sum
    

a =int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


print(multiply_1_iteration(a,b))
print(multiply_n_iterations(a,b))