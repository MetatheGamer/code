from student import Student
#create function that loads student data from students.csv file
#create objects and put in list
#return list of student objects
def load_students():
    student_list = []
    try:
        file = open("students.csv","r")
        counter = 0
        for line in file:
            counter += 1
            if counter==1:
                continue
            data = line.split(",")
            if len(data)==6:
                firstname = data[0]
                lastname = data[1]
                major = data[2]
                credit_hours = data[3]
                gpa = data[4]
                id = data[5]
                student = Student(firstname,lastname,major,credit_hours,gpa,id)
                student_list.append(student)
            else:
                raise Exception(f"There is an error in your data on line {counter}")
    except Exception as err:
        print(err)
    finally:
        file.close
    return student_list

def printStudentData(list_of_students):
    print("\nStudent Data.")
    for student in list_of_students:
        print(f"{student.get_firstName()} {student.get_lastName()}: {student.get_major()}")
        print(f"GPA: {student.get_gpa()}")
        print(f"Class: {student.get_year()}")
        print(f"ID: {student.get_ID()}\n")
    return
    
def main():
    student_list = load_students()
    printStudentData(student_list)
main()
