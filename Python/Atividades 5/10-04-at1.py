# Faça um Programa em Python que leia três números e mostre o maior e o menor
# deles.

A = int(input("Informe o valor para A: "))
B = int(input("Informe o valor para B: "))
C = int(input("Informe o valor para C: "))
if A > B and A > C:
    print("o MAIOR numero é: %s" %(A))
elif B>A and B>C:
    print("o MAIOR numero é: %s" %(B))
elif C>A and C>B:
    print("o MAIOR numero é: %s" %(C))
    
if A < B and A < C:
     print("o MENOR numero é: %s" %(A))
elif B<A and B<C:
     print("o MENOR numero é: %s" %(B))
elif C<A and C<B:
    print("o MENOR numero é: %s" %(C))