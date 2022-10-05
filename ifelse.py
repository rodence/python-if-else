print("Please input 3 integers")
num1 = int(input("Please Enter 1st number: "))
num2 = int(input("Please Enter 2nd number: "))
num3 = int(input("Please Enter 3rd number: "))


if num1 >= num2 and num1 <= num3:
    print("The Highiest number is "+ str(num1))
elif num2 >= num3:
    print("The Highiest number is "+ str(num2))
else:
    print("The Highiest number is "+ str(num3))
