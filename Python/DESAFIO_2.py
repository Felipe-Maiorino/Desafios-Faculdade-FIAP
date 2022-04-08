# Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.

def TotalDeVotosSemanas():

    print("SEGUNDA-FEIRA teve: {} Votos ".format(SegundaFeira))
    print("TERÇA-FEIRA teve: {} Votos ".format(TercaFeira))
    print("QUARTA-FEIRA teve: {} Votos ".format(QuartaFeira))
    print("QUINTA-FEIRA teve: {} Votos ".format(QuintaFeira))
    print("SEXTA-FEIRA teve: {} Votos ".format(SextaFeira))
    print("SABADO-FEIRA teve {} Votos ".format(Sabado))
    print("DOMINGO-FEIRA teve: {} Votos ".format(Domingo))
    
def ResultadoVotosSemana():


    if SegundaFeira > TercaFeira and SegundaFeira > QuartaFeira and SegundaFeira > QuintaFeira and SegundaFeira > SextaFeira and SegundaFeira > Sabado and SegundaFeira > Domingo:
        print("O dia da semana escolhido foi : Segunda-Feira")

    elif TercaFeira > SegundaFeira and TercaFeira > QuartaFeira and TercaFeira > QuintaFeira and TercaFeira > SextaFeira and TercaFeira > Sabado and TercaFeira > Domingo:
        print("O dia da semana escolhido foi : Terça-Feira")

    elif QuartaFeira > SegundaFeira and QuartaFeira > TercaFeira and QuartaFeira > QuintaFeira and QuartaFeira > SextaFeira and QuartaFeira > Sabado and QuartaFeira > Domingo:
        print("O dia da semana escolhido foi : Quarta-Feira")

    elif QuintaFeira > SegundaFeira and QuintaFeira > TercaFeira and QuintaFeira > QuartaFeira and QuintaFeira > SextaFeira and QuintaFeira > Sabado and QuintaFeira > Domingo:
        print("O dia da semana escolhido foi : Quinta-Feira")

    elif SextaFeira > SegundaFeira and SextaFeira > TercaFeira and SextaFeira > QuartaFeira and SextaFeira > QuintaFeira and SextaFeira > Sabado and SextaFeira > Domingo:
        print("O dia da semana escolhido foi : Sexta-Feira")

    elif Sabado > SegundaFeira and Sabado > TercaFeira and Sabado > QuartaFeira and Sabado > QuintaFeira and Sabado > SextaFeira and Sabado > Domingo:
        print("O dia da semana escolhido foi : Sabado \n com {} Votos".format)
    
    else:
        print("O dia da semana escolhido foi domingo")



Resposta = int(input("Deseja escolher o numero de maximo de votos? [1]sim ou [2]Não: "))
if Resposta == 1:

    # Sistema com escolha de numeros totais de votos

    Votos = int(input("Qual o maximo de votos escolhidos?: "))

    SegundaFeira = 0
    TercaFeira = 0
    QuartaFeira = 0
    QuintaFeira = 0
    SextaFeira = 0
    Sabado = 0
    Domingo = 0
      
    for NumeroDeVotos in range(Votos):
        Menu = int(input("Qual dia da semana é o melhor para realização das lives?: ([1]SEGUNDA-FEIRA, [2]TERÇA-FEIRA, [3]QUARTA-FEIRA, [4]QUINTA-FEIRA, [5]SEXTA-FEIRA, [6]SABADO OU [7]DOMINGO: "))
        if Menu == 1:
            SegundaFeira = SegundaFeira + 1
        elif Menu == 2:
            TercaFeira = TercaFeira + 1
        elif Menu == 3:
            QuartaFeira = QuartaFeira + 1
        elif Menu == 4:
            QuintaFeira = QuintaFeira + 1
        elif Menu == 5:
            SextaFeira = SextaFeira + 1
        elif Menu == 6:
            Sabado = Sabado + 1
        elif Menu == 7:
            Domingo = Domingo + 1
        else:
            print("Tente Novamente: ")    
    
    TotalDeVotosSemanas()

    ResultadoVotosSemana()

   

else: 

# Sistema sem ecolha da quantidade de votos

    Menu = -1

    SegundaFeira = 0
    TercaFeira = 0
    QuartaFeira = 0
    QuintaFeira = 0
    SextaFeira = 0
    Sabado = 0
    Domingo = 0
    EncerrarPrograma = 0

    while Menu !=8:
        Menu = int(input("Qual dia da semana é o melhor para realização das lives?: ([1]SEGUNDA-FEIRA, [2]TERÇA-FEIRA, [3]QUARTA-FEIRA, [4]QUINTA-FEIRA, [5]SEXTA-FEIRA, [6]SABADO OU [7]DOMINGO, [8]ENCERRAR PROGRAMA: "))
        if Menu == 1:
            SegundaFeira = SegundaFeira + 1
        elif Menu == 2:
            TercaFeira = TercaFeira + 1
        elif Menu == 3:
            QuartaFeira = QuartaFeira + 1
        elif Menu == 4:
            QuintaFeira = QuintaFeira + 1
        elif Menu == 5:
            SextaFeira = SextaFeira + 1
        elif Menu == 6:
            Sabado = Sabado + 1
        elif Menu == 7:
            Domingo = Domingo + 1
        elif Menu == 8:
            print("Finalizando Sistema")
        else:
            print("Tente Novamente: ")
        
    TotalDeVotosSemanas()

    ResultadoVotosSemana()
