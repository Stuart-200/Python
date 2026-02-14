word= (input("Enter the word: "))
substrings = set()
for i in range(len(word)):
    for j in range(i + 1, len(word) + 1):
        substrings.add(word[i:j])
        
print("All possible substrings:")
for substring in substrings:
    print(substring)
print(f'Total number of substrings: {len(substrings)}')