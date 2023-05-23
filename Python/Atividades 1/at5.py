# Elabore um programa em Python que dada a
# idade de um nadador classifique-o em uma das
# seguintes categorias:
# ✓ infantil A = 5 - 7 anos
# ✓ infantil B = 8-10 anos
# ✓ juvenil A = 11-13 anos
# ✓ juvenil B = 14-17 anos
# ✓ adulto = 18-25 anos
# • Mostrar mensagem “idade fora da faixa etária”
# quando outro valor for informado.

i = int(input("Informe sua idade "))
if ( i >= 5 and i <=7):
    print("Infantil A")
elif (i >= 8 and i <= 10):
    print("Infantil B")
elif (i >=11 and i <=13):
    print("Juvenil A")
elif (i >=14 and i <=17):
    print("Juvenil B")
elif (i >=18 and i <=25):
    print("Adulto")
else:
    print("Idade fora da faixa etaria")