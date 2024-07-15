num1 = int(input("Enter First Number ==>"))
operation = input("Enter the operation (+, -, *, / , % ): ")
num2 = int(input("Enter Second Number ==>"))
if operation == "+":
    ans=num1+num2
    print("Your Answer  is==>",ans)
elif operation == "-":
    ans=num1-num2
    print("Your Answer  is==>",ans)
elif operation == "*":
    ans=num1*num2
    print("Your Answer  is==>",ans)
elif operation == "/":
    ans=num1/num2
    print("Your Answer  is==>",ans)
elif operation == "%":
    if num2 != 0:
            ans = (num1 / num2) * 100
            print("Your Answer  is==>",ans)
    else:
            print("Error: Division by zero is not allowed.")
            print("Please Check Second Number input")
else:
    print("Wrong Choice Please Enter Valid Choice ...")