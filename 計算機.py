   # coding: shift-jis

operation = input("どれにしますか？ (+, -, *, /): ")

# Input the numbers
num1 = float(input("最初の数字: "))
num2 = float(input("もう一つの数字: "))

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
    print("不正です。")

