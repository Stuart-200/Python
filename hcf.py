number_largest = int(input("Enter the largest number:"))
number_smallest = int(input("Enter the smallest number:"))

while number_smallest !=0:
    
    number_store = number_smallest
    number_smallest = number_largest % number_smallest
    number_largest = number_store
    

print("HCF is:,", number_largest)