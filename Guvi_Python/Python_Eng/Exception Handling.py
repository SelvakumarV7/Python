# You are required to write a Python function to divide two numbers. Handle the ZeroDivisionError exception that may occur when the divisor is zero.

def division():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a/b)
    except ZeroDivisionError:
        print("Please provide integer values without zero")
    finally:
        print("Thanks")
d = division()