def numbers_opration():
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    if num_2 == 0:
        print("You cannot divide by zero. Please enter a valid second number.")
        num_2 = float(input("Enter the second number: "))
    return num_1, num_2





def operation_choice():
    opr = input("Enter the operation you want to do (+, -, *, /): ")
    while opr not in ['+', '-', '*' ,'/']:
        opr = input("Invalid operation. Please enter a valid operation (+, -, *, /): ")
    return opr





def calculate(num_1, num_2, opr):
    if opr == "+":
        return num_1 + num_2
    elif opr == "-":
        return num_1 - num_2
    elif opr == "*":
        return num_1 * num_2
    elif opr == "/":
        return num_1 / num_2

print(calculate(*numbers_opration(), operation_choice()))
