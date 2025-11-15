def fib(n):

   if n == 0:
     return 0
   elif n == 1:
       return 1
   else:
       return fib(n-1) + fib(n-2)
   
   

def is_fibonacci(x,i=0):
    
    if fib(i) == x:
        return True
    elif fib(i) > x:
        return False
    else:
        return is_fibonacci(x, i+1)
    
num = int(input("Enter a number: "))     
    
    


if is_fibonacci(num):
    print(num, "is a Fibonacci number")
else:
    print(num, "is not a Fibonacci number")