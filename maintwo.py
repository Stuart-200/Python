file_read = open('Codingaltwo.txt', 'r')
print("File in Read Mode: - ")
print(file_read.read())
file_read.close()



file_write = open('Codingalwo.txt', 'w')
file_write.write("File inwrite mode...")
file_write.write("Hi! I am Stuart.I am 16 years old")


file_append = open('Codingaltwo.txt', 'a')
file_append.write("\n File in append mode..")
file_append.write("Hi! I am Robin. I am 15 years old")
file_append.close()