from Add import add
from Subtract import subtract
from Divide import divide
from Multiply import multiply


def Calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {Multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {Divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    Calculator()
