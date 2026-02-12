num=int(input("Enter a number: "))
binary_n=bin(num)[2:]

count=0
max_count=0

for bit in binary_n:
    if bit == "1":
        count = count +1
        max_count = max(max_count, count)
    else:
        count = 0
print(f"Original number: {num} (binary: {binary_n})")
print(f"Maximum number of consecutive 1's: {max_count}")
