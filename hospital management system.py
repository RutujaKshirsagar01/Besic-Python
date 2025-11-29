# Hospitl management System project 

print("Welcome To Hospital Management System.")
patients = {1: {'name': 'john','age': 30, 'gender': 'M', 'disease': 'Flu', 'city':'pune','doctor': 'Dr. Smith'}}

while True:
    print("""
Operations you can do:  
    1. Create patients record
    2. Display All patients record
    3. Update patient  record
    4. Delete patient record
    5. Exit
""")
    
    ch=int(input("Enter your choice: "))
    if ch==1:
        patient = {}
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender (M/F): ")
        disease = input("Enter Disease/Condition: ")
        city=input("Enter city name:")
        doctor = input("Enter Assigned Doctor: ")

        patient['name'] = name
        patient['age'] = age
        patient['gender'] = gender
        patient['disease'] = disease
        patient['city']=city
        patient['doctor'] = doctor

        patients[pid] = patient
        print("Patient record created successfully.\n")

    elif ch==2:
        print("-"*145)
        print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".
              format("pid", 'Name', 'age', 'gender', 'disease','city','doctor name'))
        print("-"*145)
        for pid in patients:
                print("{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".
                  format(pid,patients[pid]['name'],patients[pid]['age'],
                         patients[pid]['gender'],patients[pid]['disease'],patients[pid]['city'],patients[pid]['doctor']))
                
    elif ch==3:
         pid = int(input("Enter Patient ID to update: "))
         print("""What do you want to update:
               1.Name
               2.Age
               3.Gender
               4.Disease/condition
               5.city
               6.doctor""")
         
         c=int(input("Enter your choice: "))

         if c==1:
              pname=input("Plese Enter new name: ")
              patients[pid]['name']=pname
              print("Record updated successfully.")

         elif c==2:
              page=input("Plese Enter new age: ")
              patients[pid]['age']=page
              print("Record updated successfully.")

         elif c==3:
              pgender=input("Plese Enter new gender: ")
              patients[pid]['gender']=pgender
              print("Record updated successfully.")

         elif c==4:
              pdisease=input("Plese Enter new disease: ")
              patients[pid]['disease']=pdisease
              print("Record updated successfully.")

         elif c==5:
              pcity=input("Plese Enter new city: ")
              patients[pid]['city']=pcity
              print("Record updated successfully.")

         elif c==6:
              pdocter=input("Plese Enter new docter: ")
              patients[pid]['doctor']=pdocter
              print("Record updated successfully.")

         else:
              print("Enter valid choice: ") 

    elif ch==4:
         pid=int(input("Enter patient id to delete record: "))
         del patients[pid]
         print("Record deleted successfully.")

    elif ch==5:
        print("Exiting... Thank you!")
        break

    else:
         print("Enter valid choice ")

          
                
    

