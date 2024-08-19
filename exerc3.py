print("Dê um valor para A e B")

valor1 = int(input("Valor de A: "))

valor2 = int(input("Valor de B: "))

a = valor1
b = valor2 

print("A=" ,a, "B=" ,b,)
a,b = b,a
print("A=" ,a, "B=" ,b,)