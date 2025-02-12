numero = int(input("Entre com um número inteiro: "))
inicioIntervalo = int(input("Entre com o início do intervalo: "))
fimIntervalo = int(input("Entre com o fim do intervalo: "))

print ("Tabuada do número", numero, "no intervalo de", inicioIntervalo, "a", fimIntervalo, ":")

for i in range(inicioIntervalo, fimIntervalo + 1):
    print(numero, "*", i, "=", numero * i)