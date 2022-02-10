
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def swap():
    global num1, num2
    n = num1
    num1 = num2
    num2 = n
def main():
    swap()
    print("The value of num1 after swaping: ", num1)
    print("The value of num2 after swaping: ", num2)

if __name__ == "__main__":
    main()
