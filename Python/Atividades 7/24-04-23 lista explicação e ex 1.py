# Criar um arquivo fonte, e aplicar todos os exemplos de manipulação de
# listas apresentados anteriormente.

listaVazia =[]
print(listaVazia)

listaCompras = ['arroz','feijão','massa']
print(listaCompras)

minhaLista = [1.2,555, True, listaCompras] #lista dentro de lista, essa tem 4 elementos 
print(minhaLista)

#listaCompras = ['arroz','feijão','massa']
#         indice     0       1       2

#operadpr de listas

lista =[9,4,5]
#acesso o item 0 da lista
print(lista[0])

#acesso o item 1 da lista
print(lista[1])

#acesso o item 2 da lista
print(lista[2])

#acesso o intervalo da 0 a 1
print(lista[0:2])

#acesso o intervalo da 0 a 2
print(lista[:2])

#acesso o intervalo da 1 a 0
print(lista[1:])


#concatenando listas
livros = ['java','SqlServer','Delphi','Python']
revistas = ['Java Magazine', 'Mundo Delphi','Explorando Python']
listaConcatenada = livros + revistas
print(listaConcatenada)


#Verificando a existencia de um elemento na lista
livros = ['java','SqlServer','Delphi','Python','Java']
print('Java' in livros)

#buscando valores minimo, maximo e a soma dos elementos na lista
listaNumeros = [10.50,20,10,30.50]
print(min(listaNumeros) )
print(max(listaNumeros) )
print(sum(listaNumeros) )

#Retornando o comprimento da lista
livros = ['java','SqlServer','Delphi','Python']
print(len(livros))

#Retornando o numero de ocorrencias do elemento Java na lista ( quantas vezes o Java aparece na lista, é uma conta)
livros = ['Java','SqlServer','Delphi','Python','Java']
print(livros)
print(livros.count('Java'))

#acresentar um elemento na lista ( no final dela append()  )
livros = ['Java','SqlServer','Delphi','Python']
print(livros)
livros.append('Android')
print(livros)

#Utilizando insert(i,x)
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print (livros)
livros.insert(2, 'Android')
print (livros)

#Utilizando remuve(X)
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print(livros)
livros.remove('Delphi')
print(livros)

#utilizando pop(i)
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print(livros)
livros.pop()
print(livros)
livros.pop(2)
print(livros)

#Removendo todos os itens de uma lista]
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print(livros)
livros.clear()
print(livros)

#Ordenando a lista
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print (livros)
livros.sort()
print(livros)

#Invertendo a ordem dos elementos das lista
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print(livros)
livros.reverse()
print(livros)

