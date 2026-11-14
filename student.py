name = input("Enter Student Name: ")
mark1 = float(input("Enter marks in Subject 1: "))
mark2 = float(input("Enter marks in Subject 2: "))
mark3 = float(input("Enter marks in Subject 3: "))


total = mark1 + mark2 + mark3


# Display student details
print("\n----- Student Mark Details -----")
print("Student Name:", name)
print("Subject 1 Marks:", mark1)
print("Subject 2 Marks:", mark2)
print("Subject 3 Marks:", mark3)
print("Total Marks:", total)



if mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")