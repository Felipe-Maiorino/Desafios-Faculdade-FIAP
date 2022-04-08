
print("Calculo de média da turma")

NotaTotalImpar = 0
MediaImpar = 0
MediaPar = 0
NotaTotalPar = 0


for AlunosImpares in range (1, 51, 2):
    
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES: ")
    EntradaDeNotaImpar = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NUMERO {} :".format(AlunosImpares)))

    while EntradaDeNotaImpar > 10:
        print("\n")
        print("Nota Invalida")
        EntradaDeNotaImpar = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NUMERO {} :".format(AlunosImpares)))
        


    NotaTotalImpar = NotaTotalImpar + EntradaDeNotaImpar
    
             
    print("\n")
        


for AlunosPares in range (2, 51, 2):

    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES: ")
    EntradaDeNotaPar = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NUMERO {} : ".format(AlunosPares)))

    while EntradaDeNotaPar > 10:
        print("Nota Invalida")
        EntradaDeNotaImpar = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NUMERO {} :".format(AlunosImpares)))
        print("\n")


    NotaTotalPar = NotaTotalPar + EntradaDeNotaPar
    print("\n")
    
    
MediaImpar = NotaTotalImpar / 25
MediaPar = NotaTotalPar / 25

print("A media da sala Impar foi: {}".format(MediaImpar))
print("A media da sala Par foi: {}".format(MediaPar))

if MediaImpar > MediaPar:
    print("A maior nota da sala foi da turma impar: {}".format(MediaImpar))
elif MediaImpar == MediaPar:
    print("Tanto impar quanto par obtiveram as mesmas notas {}".format(MediaImpar))
else:
    print("A maior nota da sala foi da turma Par: {}".format(MediaPar))

        




        

