def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result


students = [
    [1, 'Jean castro', 'v'],
    [2, 'Lula Foster', 'VI'],
    [3, 'Brian Howell', 'VI'],
    [5, 'Zachary Simon', 'VII']
]


print("\nOriginal list of lists:")
print(students)
print("\nConverted to dictionary:")
print(test(students))






