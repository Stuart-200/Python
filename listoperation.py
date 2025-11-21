fruitlist = ['Apple', 'Guava' , 'Mango', 'Banana', 'Kiwi']





print("lent of list :", len(fruitlist))
print("First ElementP:", fruitlist[0])
print("Last Element:", fruitlist[-1])

fruitlist.remove('Guava')
print("Updated List: " , fruitlist)


print()
fruitlist.sort()
print("Sorted List: " , fruitlist)

#

fruitlist.pop(1)
print("updated List:", fruitlist)



fruitlists = ['Apple', 'Guava' , 'Mango', 'Banana', 'Kiwi']

print(fruitlists[2:4])