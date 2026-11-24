num_1 = int(input("enter the first number: "))
opr = input("enter the opration you want to do :")
num_2 = int(input("enter the second number: "))

oprations = ['+' , '-' , '*' , '/']



while True:
    if opr not in oprations:
        opr = input("enter the valude opration plase: ")
    elif opr in oprations:
        if opr == "+":
            print(num_1 ,"+" ,num_2 , "=" , num_1 + num_2 )
            break
        elif opr == "-":
            print(num_1 ,"-" ,num_2 , "=" , num_1 - num_2 )
            break
        elif opr == "*":
            print(num_1 ,"*" ,num_2 , "=" , num_1 * num_2 )
            break
        elif opr == "/":
            if num_2 == 0:
                print("you can not divide by zero")
                num_2 = int(input("enter the second number: "))
            print(num_1 ,"/" ,num_2 , "=" , num_1 / num_2)
            break

                



    

