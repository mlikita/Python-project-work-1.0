# Write a python program to build a simple calculator
# Available operations 
# 1) Addition 
# 2)subtraction 
# 3)Multiplications  
# 4)Division 
# 5) Average

#Functions to perform operations

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def avg(num1,num2):
    return (num1+num2)/2

print("Please select a operations: \n" "1.Addition\n" "2.Subtraction\n" "3.Multiplication\n" "4.Division\n" "5.Average\n")

#user input

operation=int(input("Enter operatiors: "))
number1=int(input("Enter First number: " ))
number2=int(input("Enter Second number: "))

#if-elif-else statement

if operation==1:
    print(number1,"+",number2,"=",add(number1,number2))
elif operation==2:
    print(number1,"-",number2,"=",sub(number1,number2))
elif operation==3:
    print(number1,"*",number2,"=",mul(number1,number2))
elif operation==4:
    print(number1,"/",number2,"=",div(number1,number2))
elif operation==5:
    print("(",number1,"+",number2,")","/","2","=",avg(number1,number2))
else:
    print("\nEnter valid operations")

