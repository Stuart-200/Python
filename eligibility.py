total_days = int(input("Enter the total number of days: "))
absent_days = int(input("Enter the number of absent days: "))

attended_days = total_days - absent_days
attendence_percentage = (attended_days / total_days) * 100
print("Your attended days:", attended_days)
print("Your attendance percentage:", attendence_percentage, "%")

if attended_days <=75:
    print("You are not eligible for the exam")
else:
    print("You are eligible for the exam")