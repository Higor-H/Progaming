# Faça um programa para calcular o aumento salarial de uma pessoa. O programa deve
# receber o nome da pessoa, o salário atual do colaborador e aplicar o reajuste segundo
# percentual que consta na tabela abaixo:
# FAIXA SALARIAL                     ÍNDICE DE AUMENTO (%)
# Até R$ 1.200,00                    20%
# entre R$ 1.200,01 e R$ 1.500,00    15%
# entre R$ 1.500,01 e R$ 2.500,00    10%
# Acima de R$ 2.500,00               5%
# Após o aumento ser realizado, informe na tela:
# • o percentual (índice) de aumento aplicado;
# • o valor do reajuste;
# • o novo salário com reajuste.
# • o valor do abono.
# • o salário final.
# Para quem ganha salário até R$ 1.200,00 e possui filhos, deverá ser acrescentado
# um abono de R$ 100,00 por filho.
# Ao final da operação, o programa deve perguntar se o usuário pretende fazer um novo
# cálculo, caso sim repete a operação, caso não, finaliza a execução do programa.
# Considerações:
# • Valor do reajuste: é o valor referente ao percentual de aumento sobre o
# salário atual. Ex.: para o salário atual de 1.200,00, aplicar o índice de 20%
# conforme a tabela aumento (1200,00 /100 * 20 = 240,00).
# • Novo Salário com reajuste: é o salário atual somando o valor do valor do
# reajuste. Ex.: (1.200,00 + 240,00 = 1.440,00)
# • Valor do abono: corresponde a quantidade de filhos multiplicado por 100. Ex.:
# para 2 filhos (100 * 2 = 200,00)
# • Salário Final: corresponde ao salário com reajuste, somando o valor do
# abono. Ex.: 1.440,00 + 200,00 = 1.640,00.



op = "s"
while (op == "s"):
    nome = str(input("Nome: "))
    filho = int(input("Quantidade de Filhos: "))
    sal = float(input("Salario atual R$: "))
    print("-------------------------------")
    if sal <=1200:
        reax = sal/100*20
        rea = sal + reax
        aba = filho*100
        sf = rea + aba
        print("Indice de reajuste 20%")
        print("Valor do reajuste: %s" %(reax))
        print("Novo salario com reajuste R$: %s" %(rea))
        print("valor do abandono: %s" %(aba))
        print("Salario finalÇ: %s" %(sf))
        print("=======================================")
    elif sal >=1200.01 and sal <=1500:
        reax = sal/100*15
        rea = sal + reax
        aba = filho*0
        sf = rea + aba
        print("Indice de reajuste 15%")
        print("Valor do reajuste: %s" %(reax))
        print("Novo salario com reajuste R$: %s" %(rea))
        print("valor do abandono: %s" %(aba))
        print("Salario finalÇ: %s" %(sf))
        print("=======================================")
    elif sal >=1500.01 and sal <=2500:
        reax = sal/100*10
        rea = sal + reax
        aba = filho*0
        sf = rea + aba
        print("Indice de reajuste 10%")
        print("Valor do reajuste: %s" %(reax))
        print("Novo salario com reajuste R$: %s" %(rea))
        print("valor do abandono: %s" %(aba))
        print("Salario finalÇ: %s" %(sf))
        print("=======================================")
    elif sal >2500:
        reax = sal/100*5
        rea = sal + reax
        aba = filho*0
        sf = rea + aba
        print("Indice de reajuste 5%")
        print("Valor do reajuste: %s" %(reax))
        print("Novo salario com reajuste R$: %s" %(rea))
        print("valor do abandono: %s" %(aba))
        print("Salario finalÇ: %s" %(sf))
        print("=======================================")
    op = str(input("Informe [s] para fazer um novo cálculo ou [n] para sair: "))
    