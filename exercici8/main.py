
num1 = int(input("Enter x: "))
num2 = int(input("Enter y: "))

def power():
    prod = 1
    for i in range(num2):
        prod = prod * num1
        print("The value is:", prod)

def main():
    power()

if __name__ == "__main__":
    main()
