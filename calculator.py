def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return("cant be divided by 0")
  
print("1: +")
print("2: -")
print("3: *")
print("4: /")
operator = input("select the operation: ") 


num1 = int(input("enter the frist number: "))
num2 = int(input("enter the second number: "))

if operator == ("+"):
    sum = (add(num1, num2))
elif operator == ("-"):
    sum = (substract(num1, num2))   
elif operator == ("*"):
    sum = (multiply(num1, num2)) 
elif operator == ("/"):
    sum = (divide(num1, num2))
else:
    print("invalid operator")

print(f"the sum of the number {(num1)} and {(num2)} is {(sum)}. ") 