school_age=5
school_max_age=7
print("The Minimum age is: 5")
student_age=input("Please Enter the age of student ")    #input function
student_age=int(student_age)                      #change data type
if student_age==school_age:                       #if statement
    print("Admission confirmed")
elif student_age < school_age:                    #elif statement is used
    print("Age is too less")
elif student_age >= school_max_age:
    print("Age too much")
else:                                             #else statement
    print("admission not confirmed")




    