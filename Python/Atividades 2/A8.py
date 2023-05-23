#Faça um programa em Python para:
#Ler a descrição do produto (nome), a quantidade adquirida e o preço unitário.
#Calcular e escrever o total (total = quantidade adquirida * preço unitário), o valor do desconto e o
#total a pagar (total a pagar = total - desconto), sabendo-se que:
# - Se quantidade <= 5 o desconto será de 2%
# - Se quantidade > 5 e quantidade <=10 o desconto será de 3%
# - Se quantidade > 10 o desconto será de 5%


nome = str(input("Nome do produto: "))
q = int(input("Quantidade do produto: "))
v = float(input("Valor unitário R$: "))
print("---------------------------------------------------------------------")
if (q <= 5):
    va = float((v * q) * 0.02)
    print ("Valor do desconto R$: %s" % (va))
    vt = ((v * q) - va)
    print("Valor TOTAL à pagar R$: %s" % (vt))
elif (q > 5 and q <= 10):
    va = float((v * q) * 0.03)
    print ("Valor do desconto R$: %s" % (va))
    vt = ((v * q) - va)
    print("Valor TOTAL à pagar R$: %s" % (vt))
elif (q > 10):
    va = float((v * q) * 0.05)
    print ("Valor do desconto R$: %s" % (va))
    vt = ((v * q) - va)
    print("Valor TOTAL à pagar R$: %s" % (vt))