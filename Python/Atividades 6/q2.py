# Faça um programa em Python para contar e mostrar a quantidade de números que são
# divisíveis por 3 entre um intervalo informado pelo usuário. Ao final da operação solicite se o usuário deseja
# repetir ou encerrar, conforme apresentado na imagem. Para verificar se um número é divisível por 3,
# basta testar se o resto da divisão por 3 é igual à zero: ( variável % 3 == 0 ). 

op = "s"
while op == "s":
    soma = 0
    print("----------------------------------")
    ini = int(input("Informe um número inicial: "))
    fin = int(input("Informe um número final: "))
    for i in range (ini, fin +1):
        if i % 3 == 0:
            soma = soma + 1
    print("A soma  dos números divisíveis por 3 foi: %s" %(soma))
    op = str(input("Informe [s] para repetir a operação ou [n] para encerrar: "))
    
    
