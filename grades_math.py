if logged_in==True:
    input_grade="Yes"
    gradeNumber=0
    grades=[]
    while input_grade=="Yes":
        gradeNumber+=1
        studentName=input("What is the name of the student? ")
        studentGrade=float(input("What is the student's number grade? "))
        if studentGrade>=90:
            studentLetter="A"
        elif studentGrade<90 and studentGrade>=80:
            studentLetter="B"
        elif studentGrade<80 and studentGrade>=70:
            studentLetter="C"
        elif studentGrade<70 and studentGrade>=60:
            studentLetter="D"
        elif studentGrade<60:
            studentLetter="F"
        print()
        print(f"Student name: {studentName}")
        print(f"Student grade: {studentGrade}, {studentLetter}")
        print()
        grades.append(studentGrade)
        input_grade=input("Do you want to input another grade? (Yes/No) ")

    calc=input("Calculate average? (Y/N) ")
    if calc == "Y":
        average=0
        for number in grades:
            average=average+number
        average/gradeNumber
        print(f"The average grade is: {average}")
else:
    pass
