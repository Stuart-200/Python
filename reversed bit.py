def reversed_bits(n):
    reversed=0
    bit_lenth=n.bit_length()
    for i in range(bit_lenth):
        reversed= (reversed << 1) | (n & 1) 
        n >>= 1
    return reversed

num=int(input("Enter a number: "))
binary_n=bin(num)[2:]
reversed_number = reversed_bits(num)
reversed_binary = bin(reversed_number)[2:].zfill(len(binary_n))
print(f"Original number: {num} (binary: {binary_n})")
print(f"Reversed bits: {reversed_number} (binary: {reversed_binary})")