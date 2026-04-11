class Student:
    def __init__(self,name,roll_no,subject):
        self.name = name
        self.roll_no = roll_no
        self.subject = subject
        
    def introduce(self):
        return f"Name of student {self.name}\nRoll no:- {self.roll_no}\nSubject : {self.subject}"
    
student1 = Student("Akash",2304324,'ML')
student2 = Student("Ankit",2304327,"NN")

print(student1.introduce())