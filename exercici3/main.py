def decimaltobinary(num):
  if num > 1:
    decimaltobinary(num // 2)
  print(num % 2, end="")
numero=int(input("Entra un numero: "))

def main():
    decimaltobinary(numero)

if __name__ == "__main__":
    main()
