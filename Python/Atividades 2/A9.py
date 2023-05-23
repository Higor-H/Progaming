#Faça um programa em Python que:
#• Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa.
#• Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda,
#segundo a tabela:
#Renda                           Imposto
#de 0.00 a R$ 2000.00            Isento
#de R$ 2000.01 até R$ 3000.00    8%
#de R$ 3000.01 até R$ 4500.00    18%
#acima  de R$ 4500.00            28%

s = float(input("Informe seu salario: "))
if ( s <= 2000):
    print("Isento")
elif ( s >= 2000.01 and s <= 3000.00):
    mi =( s - 2000)
    m2 = ( mi * 0.08)
    print("R$ %s" % (m2))
elif ( s >3000.01 and s <= 4500):
    m3 = (s - 3000)
    m33 =(( m3 * 0.18) + 80)
    print("R$ %s" % (m33))
elif ( s > 4500):
    m4 = (s - 4500)
    m44 = (( m4 * 0.28) + 350)
    print("R$ %s" % (m44))