   # coding: shift-jis

operation = input("�ǂ�ɂ��܂����H (+, -, *, /): ")

# Input the numbers
num1 = float(input("�ŏ��̐���: "))
num2 = float(input("������̐���: "))

# Perform the operation
if operation == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif operation == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operation == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif operation == "/":
    result = num1 / num2
    print(num1, "/", num2, "=", result)
else:
    print("�s���ł��B")

