# A partir do código disponibilizado em Python,
# incremente o mesmo da seguinte forma: • Mostre o contador de vendas; • A cada fim de operação, o programa deve
# perguntar se o usuário deseja fazer mais uma
# operação. Se for informado sim [s] o programa
# deve repetir a operação, se não [n] o programa
# deve ser encerrado.
# • Ao final da execução do programa, o mesmo
# deve apresentar a mensagem de caixa
# encerrado.


cont = 0
op = "s"
while (op == "s"):
    cont = cont + 1
    print("VENDA %s ================================================" % (cont))
    produto = input("Nome do produto: ")
    quant = float(input("Quantidade do produto: "))
    valorUnit = float(input("Valor unitário R$ : "))
    totalCompra = quant * valorUnit
    if(quant <= 5) :
        desc = totalCompra * 0.02
    elif (quant > 5 and quant <= 10):
        desc = totalCompra * 0.03
    else:
        desc = totalCompra * 0.05
    totalPagamento = totalCompra - desc
    print("---------------------------------------")
    print("Valor do total da compra foi R$: ",totalCompra)
    print("Valor do desconto R$: ",desc)
    print("Valor TOTAL à pagar R$: ",totalPagamento)
    op = str(input("Informe [s] para repetir a operação ou [n] para sair: "))
else:
    print("CAIXA ENCERRADO ===========================================")