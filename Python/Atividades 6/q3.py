# Uma espécie de alga cresce de modo que a área ocupada pela mesma em um lago é
# igual ao dobro da cobertura do dia anterior. Um pesquisador está estudando esta espécie e quer saber,
# para uma quantidade inicial de algas, quantos dias ela levará para ocupar um dos lagos disponíveis na
# estação de pesquisa. Escreva um programa Python que leia dois valores float: a área inicial (INI) ocupada
# pela alga no início do experimento e a área total do lago (TOT). O programa deve exibir (com duas casas
# decimais) a evolução da área coberta pela alga, dia a dia, desde o primeiro dia do experimento, enquanto
# houver área disponível para o crescimento. Se algum dos valores informados for menor ou igual à zero
# ou se a área total informada (TOT) for inferior à área inicial (INI), apenas exibir a mensagem “Impossível
# realizar o experimento”.

ini = float(input("Informe a área inicial ocupada pela alga: "))
tot = float(input("Informe a área total do lago: "))
cont = 2
ssoma =0
if (ini <= 0 or tot <=0) or (tot < ini):
    print("Impossível realizar o experimento")
else:
    print("Dia 1: %s" %(ini))
    soma =ini*2
    if (soma *2) < tot:
        soma = ini *2
        if (soma *2) < tot:
            print("Dia 2: %s" %(soma))
            ssoma = soma
            if (soma *2) < tot:
                while ssoma <= tot:
                    ssoma = ssoma *2
                    cont = cont + 1
                    print("Dia %s: %s" %(cont,ssoma))
                    if (ssoma*2) > tot:
                        break
        
       
