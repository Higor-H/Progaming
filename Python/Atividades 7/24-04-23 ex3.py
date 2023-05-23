# Criar um programa em Python que crie um menu de opções, conforme
# apresentado abaixo:
# 1. Definir o tamanho de uma lista de nomes;
# 2. Inserir os nomes na lista, conforme o tamanho da lista;
# 3. Pesquisa e retorna se existe a ocorrência de um nome na lista;
# 4. Exclui um nome da lista;
# 5. Exibir os elementos da lista;
# 6. Finalizar.


print("MENU DE OPÇÕES")
print("1 - Tamanho da lista")
print("2 - Inserir nomes")
print("3 - Pesquisar nome")
print("4 - Excluir nome da lista")
print("5 - Exibir lista")
print("6 - Sair")
print("-----------------------------------")
lista = []
op = 99
while (op == 99):
    menu = int(input("Informe a opção que deseja executar: "))
    if menu == 1:
        umtam = int(input("Informe o tamanho da lista: "))
        print("-----------------------------------")
    if menu == 2:
        cont = -1
        for i in range (umtam):
            cont = cont+1
            nomein = (input("Informe o nome %s: " %(cont)))
            lista.append(nomein)
        print(lista)
        print("-----------------------------------")
    if menu ==3:
        pesq = input("informe o nome que deseja pesquisar: ")
        opa = pesq in lista
        if opa == True:
            print("Nome Localizado")
        else:
            print("Nome não Localizado")
            print("-----------------------------------")
    if menu ==4:
        remv = input("Informe o nome que deseja excluir: ")
        lista.remove(remv)
        print("-----------------------------------")
    if menu == 5:
        print(lista)
        print("-----------------------------------")
    if menu == 6:
        op = 69
    
        
        

    
            
        
        
        
        