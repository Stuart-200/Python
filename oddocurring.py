def oddOcurring(arr):
    
    res =0
    
    for element in arr:
        
       res=res^element
    
    return res

arr=[]

n=int(input("Enter the size of array: "))

while(n):
    
    num=int(input("Enter the number: "))
    arr.append(num)
    n-=1
    
print("\n odd occurring number is: ", oddOcurring(arr))


