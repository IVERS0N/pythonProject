
def decimaltobinary(num):
  if num > 1:
    decimaltobinary(num // 2)
  print(num % 2, end='')
numero=int(input("Entra un numero: "))
decimaltobinary(numero)
