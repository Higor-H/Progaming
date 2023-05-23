# Faça um programa que lê duas notas válidas (entre 0.0 e 10.0) obtidas por um aluno.
# • Ao Informar a N1(nota 1) ou a N2(nota 2), o programa deve verificar se a nota
# digitada é válida. Caso seja uma nota inválida, o programa deve exibir a
# mensagem “NOTA INVÁLIDA! Repita a operação para N(x)”, conforme
# apresentado na imagem do teste “a)”, tanto para N1 quanto para N2.
# • Quando usuário informar as notas válidas, o programa deve calcular e exibir a
# média e o conceito final, conforme apresentado em todos os testes. O conceito
# final deve ser verificado na tabela abaixo.
# • Se o aluno recebeu média 10.0, o problema deve incluir a mensagem
# “PARABÉNS! Você é um(a) aluno(a) nota 10.”

n1 = float(input("Informe uma nota valida [entre 0.0 e 10.0] para N1: "))
while (n1 < 0 or n1 > 10): 
    n1 = float(input("NOTA INVALIDA! repita o valor para N1: "))
n2 = float(input("Informe uma nota valida [entre 0.0 e 10.0] para N2: "))
while (n2 < 0 or n2 > 10): 
    n2 = float(input("NOTA INVALIDA! repita o valor para N2: "))
m = (n1+n2)/2
if m >= 9.0 and m < 10.0 :
    print("Média: %s" %(m))
    print("Conceito A")
elif m >= 7.5 and m<=8.9 :
    print("Média: %s" %(m))
    print("Conceito B")
elif m >= 6.0 and m<=7.4 :
    print("Média: %s" %(m))
    print("Conceito C")
elif m >= 4.0 and m<=5.9 :
    print("Média: %s" %(m))
    print("Conceito D")
elif m >= 0.0 and m<=3.9 :
    print("Média: %s" %(m))
elif m == 10.0 :
    print("Média: %s" %(m))
    print("Conceito A")
    print("PARABENS! Voce é um(a) aluno(a) nota 10...")
    