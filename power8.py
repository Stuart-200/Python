def powerof8(number):
    count = 0

    # check if number is a power of 2
    if number > 0 and (number & (number - 1)) == 0:

        while number > 1:
            number = number >> 1
            count += 1

        if count % 3 == 0:
            return True

    return False


number = int(input("Enter a number: "))

if powerof8(number):
    print(number, "is a power of 8")
else:
    print(number, "is not a power of 8")
