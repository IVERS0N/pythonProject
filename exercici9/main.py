

binary = input("Enter a binary code: ")

def binarytodecimal():
    decimal = 0
    for i in binary:
        decimal = decimal * 2 + int(i)
        print(decimal)
def main():
    binarytodecimal()

if __name__ == "__main__":
    main()
