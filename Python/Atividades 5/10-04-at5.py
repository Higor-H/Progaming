# Faça um programa em Python que apresente na tela um menu de opções de
# produtos e solicite como entrada, a escolha de um item do menu a partir do
# código do produto.
# Após o usuário escolher a opção, o programa deve exibir o valor do item
# escolhido.

print("CÓD------PRODUTO--------PREÇO--")
print(" 1   Cachorro Quente   R$ 10.50")
print(" 2   X-Salada          R$ 16.50")
print(" 3   Torrada Simples   R$  6.70")
print(" 4   Refrigerante      R$  5.00")
print("Faça seu pedido----------------")
i = int(input("Informe o codigo dos produto: "))
if i == 1:
    print("PEDIDO FECHADO-----------------")
    print("Você escolheu o inten de valor R$: 10.50")
elif i ==2:
    print("PEDIDO FECHADO-----------------")
    print("Você escolheu o inten de valor R$: 16.50")
elif i ==3:
    print("PEDIDO FECHADO-----------------")
    print("Você escolheu o inten de valor R$: 6.70")
elif i ==4:
    print("PEDIDO FECHADO-----------------")
    print("Você escolheu o inten de valor R$: 5.00")
elif i!= 1 and i!= 2 and i!= 3 and i!= 4:
    print("Codigo invalido")
    
    