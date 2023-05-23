# Criar um programa em Python que cria uma lista original de países
# contendo os seguintes elementos: ("Brasil", "Argentina", “Uruguai”,
# “Paraguai"). A partir desta lista, executar as seguintes manipulações
# apresentadas abaixo:
# Lista original: ['Brasil', 'Argentina', 'Uruguai', 'Paraguai']
# Foram encontrados 4 elementos na lista original.
# Foi encontrada 1 ocorrência de 'Paraguai' na lista original.
# O terceiro elemento encontrado na lista original foi: Uruguai
# Foi adicionado México no índice 2 da lista original: ['Brasil', 'Argentina', 'México', 'Uruguai', 'Paraguai Nova lista ordenada: ['Argentina', 'Brasil', 'México', 'Paraguai', 'Uruguai'] O país 'França' foi localizado na lista: False
# O país 'Brasil' foi removido da lista: ['Argentina', 'México', 'Paraguai', 'Uruguai']
# A lista foi invertida: ['Uruguai', 'Paraguai', 'México', 'Argentina']

listaori= ['Brasil','Argentina','Uruguai',
'Paraguai']
print("Lista original %s" %(listaori))

dois = len(listaori)
print("Foram encontrados %s elementos na lista original" %(dois))

tres = listaori.count('Paraguai')
print("Foi encontrada %s ocorrencia de 'Paraguai' na lista original." %(tres))

quatro = (listaori[2])
print("O terceiro elemento encoontrado na lista original foi: %s" %(quatro))

listaori.insert(2,'México')
print("Foi adicionado México no índice 2 da lista original: %s" %(listaori))

listaori.sort()
print("Nova lista ordenada: %s" %(listaori))

seis = ('França' in listaori)
print("O país 'França' foi localizado na lista: %s" %(seis))

listaori.remove('Brasil')
print("O país 'Brasil' foi removido da lista: %s" %(listaori))

listaori.reverse()
print("A lista foi invertida: %s" %(listaori))
      