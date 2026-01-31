def firstSetBit(n):


    count = 1


    while n:

        if n & 1 == 1:

            break

        count += 1

        n >>= 1

    return count

number=int(input("Enter the number:"))

result = firstSetBit(number)

print("The position of the first set bit is:", result)