
print("MENU")

print("Valor das Fotocópias: ")

print("10 fotocópias = R$ 0,25" "\n0 fotocópias = R$ 0,20" "\nMais de 20 = R$ 0,10")

ft = int(input("Digite a quantidade de Fotocópias: "))

if ft <= 10:
    print("Total a pagar: " , ft*0,25)
    
if ft >10 and ft <=20:
    print("O total a pagar é: " , ft*0,20)
    
if ft >20:
    print("O total a pagar é: " , ft*0,10)