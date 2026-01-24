from math import sqrt
two_digit_primes = []
               
for num in range(10,100):
    
    is_prime = True

    for i in range(2, int(sqrt(num)) + 1):

        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:
        two_digit_primes.append(num)\

print("The two-digit prime numbers are:", two_digit_primes)

