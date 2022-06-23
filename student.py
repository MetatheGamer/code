#create a student class with the following
#first name
#last name
#major
#class_level (freshman, sophomore, junior, senior)
#GPA
#create get/set methods where appropriate
#ID number

class Student_Class:
    def __init__(self, firstName,lastName,major,classLevel,gpa,ID):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__major = major
        self.__classLevel = classLevel
        self.__gpa = gpa
        self.__ID = ID

    def get_firstName(self):
        return self.__firstName
    def get_lastName(self):
        return self.__lastName
    def get_major(self):
        return self.__major
    def get_classLevel(self):
        return self.__classLevel
    def get_gpa(self):
        return self.__gpa
    def get_ID(self):
        return self.__ID
    
    def set_firstName(self,nfirstName):
        self.__firstName = nfirstName
    def set_lastName(self,nlastName):
        self.__lastName = nlastName
    def set_major(self,Nmajor):
        self.__major = Nmajor
    def set_classLevel(self,NclassLevel):
        self.__classLevel = NclassLevel
    def set_gpa(self,Ngpa):
        self.__gpa = Ngpa
