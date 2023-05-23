# dado um valor total da compra em reais e o numero de prestações desejadas,
# • incremente a taxa de juros sobre o valor total da compra, sendo:
# ✓ 5% até 5 prestações
# ✓ 10% de 6 a 12 prestações
# • mostre o valor total dos juros
# • mostre o valor total da compra incluindo os juros,
# • mostre o valor da prestação.
# Considerar as seguintes regras:
# • O numero mínimo de prestações é 2 e máximo é 12
# • Perguntar para o usuário, se o mesmo deseja fazer mais algum cálculo, caso sim,
# executar novamente a operação, caso não, o programa deve ser encerrado.

print("------------------------------------------------------")
print("------------------INICIANDO OPERAÇÂO------------------")
op = "s"
while (op == "s"):
    vt = float(input("Informe o valor total da compra: "))
    q = int(input("Informe a quantidade de prestação entre 2 e 12: "))
    while (q >=13 or q <= 1):
        q = int(input("Quantidade de parcelas invalidas! Informe um número entre 2 e 12: "))

    if q <= 5 :
        ja = vt * 0.05
        bah = 5
    else:
        ja = vt * 0.10
        bah = 10
    vtt = vt + ja
    par = vtt / q
    print("------------------RESULTADO------------------")
    print("O valor da compra informado foi: R$ %s" % (vt))
    print("Número de parcelas informado: %s" % (q))
    print("Taxa de juros aplicado: %s" % (bah))
    print("Valor dos juros: R$ %s" % (ja))
    print("Valor da parcela: R$ %s" % (par))
    print("Valor total: R$ %s " % (vtt))
    print("------------------FIM DA OPERAÇÃO------------------")
    print("------------------------------------------------------")
    op = str(input("Informe [s] para fazer um novo cálculo ou [n] para sair: "))
    