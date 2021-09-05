class Student:

    student_count = 0

    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        Student.student_count += 1

    def add_student():
        name = input("Enter Student's Name: ")

        while True:
            roll_no = int(input("Enter Student's Roll. no: "))

            if roll_no in u:
                print("roll no already present, Try again... \n")
                continue

            else:
                u.append(roll_no)
                break

        marks = int(input("Enter Student's marks: "))
               
        a = Student(name,roll_no,marks)

        l.append(a)

    def display_all():
        if l == []:
            print("There are no Students \n")
        else:
            for i in l:
                print("\nName : ",i.name,"\nRoll no: ",i.roll_no,"\nMarks: ",i.marks)
    
    def display(rno):
        i_d = 0
    
        for i in u:
            if i == rno:
                i_d = i

        if i_d == 0:
            print("There is No Student of that Roll No. \n")
        else:
            ind = u.index(rno)
            print("\nName : ",l[ind].name,"\nRoll no: ",l[ind].roll_no,"\nMarks: ",l[ind].marks)

    def update(roll_no):
        i_d = "0"
        
        for i in u:
            if i == roll_no:
                i_d = u.index(i)

        if i_d == "0":
            print("There is No Student of that Roll No. \n")

        else:
            ind = u.index(roll_no)
            
            if roll_no == l[ind].roll_no:
                inp = int(input("Update: \n1) Roll no \n2) Name \n3) Mark \n4) Exit  \n"))

                if inp == 1:
                    while True:
                        r_no = int(input("Enter new roll no: "))

                        if r_no in u:
                            print("roll no already present, Try again...  \n")
                            continue

                        else:
                            l[ind].roll_no = r_no
                            ui = u.index(roll_no)
                            u[ui] = r_no
                            break
                    return

                if inp == 2:
                    n = input("Enter the Name: ")
                    l[ind].name = n
                    return

                if inp == 3:
                    m = int(input("Enter the Marks: "))
                    l[ind].marks = m
                    return

                if inp == 4:
                    print("exiting... \n")
                    return

                if inp < 4 or inp > 1:
                    print("Try again  \n")

            else:
                pass
    
    @classmethod
    def Display_no_of_Students(cls):
        print("The total no. of Students present: ",Student.student_count)
        print()

    @classmethod
    def Remove_Student(cls,r):
        id =u.index(r)
        del l[id]
        del u[id]
        Student.student_count -= 1

        
l = []
u = []

while True:
    print("\n1) Add \n2) Update \n3) Display all \n4) Display One student's info \n5) Display Student count \n6) Remove Student \n7) Exit \n")
    n = int(input())

    if n == 1:
        Student.add_student()
        
    if n == 2:
        if l == []:
            print("There are no Students \n")

        else:
            p = int(input("enter the student's roll no:"))
            Student.update(p)           

    if n == 3:
        Student.display_all()

    if n == 4:
        if l == []:
            print("There are no Students ")
        else:
            inp = int(input("Enter the Student's Roll no: "))
            Student.display(inp)

    if n == 5:
        Student.Display_no_of_Students()

    if n == 6:
        if l == []:
            print("There are no Students ")
        else:
            r = int(input("Enter Student's roll no: "))
            Student.Remove_Student(r)

    if n == 7:
        print("Exiting...")
        break
        
    else:
        continue
