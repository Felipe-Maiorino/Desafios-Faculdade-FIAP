
FaturamentoAnual = float(input("Insira seu FATURAMENTO ANUAL: R$"))

AssinaturaCliente = str(input("Informe o de tipo de assinatura (BASIC, SILVER, GOLD, PLATINUM): ")).upper()

Assinatura = False

while Assinatura is False: 
    if AssinaturaCliente.upper() == "BASIC":
        BonusCliente = FaturamentoAnual * 0.3
        Assinatura = True
    elif AssinaturaCliente.upper() == "SILVER":
        BonusCliente = FaturamentoAnual * 0.2
        Assinatura = True
    elif AssinaturaCliente.upper() == "GOLD":
        BonusCliente = FaturamentoAnual * 0.1
        Assinatura = True
    elif AssinaturaCliente.upper() == "PLATINUM":
        BonusCliente = FaturamentoAnual * 0.05
        Assinatura = True
    else:
        print("Assinatura não existente \n ")
        AssinaturaCliente = str(input("Informe o de tipo de assinatura (BASIC, SILVER, GOLD, PLATINUM): ")).upper()

print("O bônus que deve ser peago é de R$ {} ".format(BonusCliente))