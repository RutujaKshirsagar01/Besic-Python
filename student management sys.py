#curd opereion 
# 1. c-create record
#  2.r-read record 
# 3.u-update record 
# 4.d-delete record 

#student management system project

# additional operetions to add
# 1.search by course 
# 2. search by name 
# 3. max marks and min marks 
# 4.to display marks>=60 
# 5.total marks 
# 6.marks asc and desc order 



print("Welcome To Student Management System.")
student={1:{'name':'john','course':'python','marks':78,'city':'pune'}}

while True:
    print(""" Operation you can do:  
          1.create record
          2.display record
          3.update record
          4.delete record
          5.search record
          6.maximum marks record
          7.minimum marks record
          8.marks is >=60 record
          9.Total marks display 
          10.Marks as asecnding order
          11.Marks as decending order
          12.pass or fail
          13.Exit""")
    ch=int(input("Enter your Choice: "))
    if ch==1:
        details={ }
        rollno=int(input("Enter Rollno:"))
        name=(input("Enter Name: "))
        course=(input("Enter Course: "))
        marks=int(input("Enter Marks: "))
        city=(input("Enter City: "))

#var[key]=values
        details['name']=name
        details['course']=course
        details['marks']=marks
        details['city']=city
        student[rollno]=details
        #print(student)
        print("Record created successfully.")

    elif ch==2:
        print("-"*105)
        print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".
              format("Roll No", 'Name', 'Course', 'Marks', 'City'))
        print("-"*105)
        for rollno in student:
            print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".
                  format(rollno,student[rollno]['name'],student[rollno]['course'],
                         student[rollno]['marks'],student[rollno]['city']))
    
    elif ch==3:
        rollno=int(input("Enter rollno: "))
        
        print(""" Operation you can do:
              1.name
              2.course
              3.marks
              4.city""")
        choice=int(input("Enter your choice: "))
        if choice==1:
            uname=input("Plese Enter new name: ")
            student[rollno]['name']=uname
            print("Record updated successfully.")
        elif choice==2:
            ucourse=input("Plese Enter new corse: ")
            student[rollno]['course']=ucourse
            print("Record updated successfully.")
        elif choice==3:
            umarks=int(input("Plese Enter new marks: "))
            student[rollno]['marks']=umarks
            print("Record updated successfully.")
        elif choice==4:
            ucity=input("Plese Enter new name: ")
            student[rollno]['city']=ucity
            print("Record updated successfully.")    
        else:
            print("Please Enter valid information")

    elif ch==4:
        rollno=int(input("Enter rollno to delete information: "))
        del student[rollno]
        print("Record deleted successfully.")

    elif ch==5:
        print(""" Search by:
              1.Name 
              2.course""")
        opt=int(input("Enter your choice: "))

        if opt==1:
            sname=input("Enter the name to search: ")
            for rollno in student:
                if student[rollno]['name']==sname:
                    s = student[rollno]
                    print(f"Found: Roll No: {rollno}, Name: {s['name']}, Course: {s['course']},Marks: {s['marks']}, City: {s['city']}")

        elif opt==2:
            scourse = input("Enter course to search: ")
            for rollno in student:
                if student[rollno]['course']==scourse:
                    s = student[rollno]
                    print(f"Found: Roll No: {rollno}, Name: {s['name']}, Course: {s['course']}, Marks: {s['marks']}, City: {s['city']}")

        else:
            print("No matching record found.")

    elif ch == 6:
        max_marks = -1
        max_rollno = None
        for rollno in student:
            if student[rollno]['marks'] > max_marks:
                max_marks = student[rollno]['marks']
                max_rollno = rollno
        if max_rollno is not None:
            s = student[max_rollno]
            print(f"Student with Max Marks: Roll No: {max_rollno}, Name: {s['name']}, Marks: {s['marks']}")


    elif ch == 7:
        min_marks = 101  
        min_rollno = None
        for rollno in student:
            if student[rollno]['marks'] < min_marks:
                min_marks = student[rollno]['marks']
                min_rollno = rollno
        if min_rollno is not None:
            s = student[min_rollno]
            print(f"Student with Min Marks: Roll No: {min_rollno}, Name: {s['name']}, Marks: {s['marks']}")

    elif ch == 8:
        print("Students with marks >= 60:")
        for rollno in student:
            if student[rollno]['marks'] >= 60:
                s = student[rollno]
                print(f"Roll No: {rollno}, Name: {s['name']}, Marks: {s['marks']}")

    elif ch == 9:
        total = 0
        for rollno in student:
            total += student[rollno]['marks']
        print(f"Total Marks of All Students: {total}")

    elif ch == 10:
        sorted_list = list(student.items())
        for i in range(len(sorted_list)):
            for j in range(i + 1, len(sorted_list)):
                if sorted_list[i][1]['marks'] > sorted_list[j][1]['marks']:
                    sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
        print("Students sorted by marks (Ascending):")
        for item in sorted_list:
            rollno = item[0]
            s = item[1]
            print(f"Roll No: {rollno}, Name: {s['name']}, Marks: {s['marks']}")

    elif ch == 11:
        sorted_list = list(student.items())
        for i in range(len(sorted_list)):
            for j in range(i + 1, len(sorted_list)):
                if sorted_list[i][1]['marks'] < sorted_list[j][1]['marks']:
                    sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
        print("Students sorted by marks (Descending):")
        for item in sorted_list:
            rollno = item[0]
            s = item[1]
            print(f"Roll No: {rollno}, Name: {s['name']}, Marks: {s['marks']}")

    elif ch == 12:
        print("Exiting... Thank you!")
        break

    else:
        print("Please Enter valid information")