students = ("ahmad", "ali", "sara", "john", "emma" , "michael", "sophia", "daniel", "olivia", "james")




def student_numbers():
    number_list = []
    for student in range(len(students)):  
        stu = input(f"enter the number for {students[student]}: ")
        stu = int(stu)
        while True:
            if stu < 0 or stu > 20:
                st = input(f"plase enter a valuid number for {students[student]}: ")
                stu = int(st)
            else:
                break
        number_list.append(stu)
    return number_list

student_number_lis =student_numbers()



def student_result():
    for i in student_number_lis :
        if 9 >= i >=0:
            print("You'r out! ")
        elif 10 <= i <= 16:
            print("you'r win! ")
        elif 20 >= i > 16:
            print("you'r the best! ")

print(student_result()) 

