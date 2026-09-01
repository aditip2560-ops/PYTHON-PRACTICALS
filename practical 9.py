#student marks management system

marks=[]

while True:
    print("\n ---- student marks management system ----")
    print("1. Insert Marks")
    print("2. Display Marks")
    print("3. update Marks")
    print("4. Delete Marks")
    print("5. Exit Marks")
    
    Choice = int(input("Enter your choice:"))
    
    # Insertion
    if Choice == 1:
          mark = int(input("Enter students marks: "))
          marks.append(mark)
          print("Marks inserted successfully.")
          
    # Traversal
    elif Choice == 2:
        if len(marks)==0:
            print("No marks available.")
        else:
            print("student Marks:")
            for i in range(len(marks)):
                print("student",i+1,":", marks[i])
                
    #Updating
    elif Choice == 3:
         student = int(input("Enter student number to update:"))
         if 1 <= student <= len(marks):
             new_mark = int(input("Enter new marks:"))
             marks[student - 1] = new_mark
             print("Marks update successfully.")
         else:
            print("Invalid student number.")
            
    #Deletion
    elif Choice == 4:
        student = int(input("Enter student number to delete:"))
        if 1 <= student <= len(marks):
            marks.pop(student - 1)
            print("Marks deleted successfully.")
        else:
            print("Invalid student number.")
            
    #Exit
    elif Choice == 5:
        print("Program ended:")
        break
    
    else:
        print("Invalid Choice.")
        