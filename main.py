def decimal_to_binary(n):
    if n==0:
        return "0"
    
    binary = ""
    while n > 0:
        reminder = n%2
        binary = str(reminder) + binary
        n = n//2
    return binary

number = int(input("Enter a decimal number: "))
binary_representation = decimal_to_binary(number)
print(f"The binary representation of {number} is {binary_representation}")