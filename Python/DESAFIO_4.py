
Minutos = int(input("FAVOR INSIRA OS MINUTOS DO RELÓGIO DE SEU COMPUTADOR: "))

Calculo = Minutos
Fatorial = 1

while Calculo > 0 :
    Fatorial *= Calculo
    Calculo -= 1

print("A senha Para liberar o sistema é")
print("LIBERDADE{}".format(Fatorial))


