for i in range(5):
    name = input("Enter the name of student : ")
    total_marks = 0
    for j in range(5):
        mark = float(input("Enter mark for subject : "))
        total_marks += mark
    print(f"Student Name: {name}, Total Marks: {total_marks}")
