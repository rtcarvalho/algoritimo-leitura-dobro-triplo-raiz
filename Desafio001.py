print('Desasfio006 = Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada:')

num1 = int(input('Digite um valor qualquer: '))

dobro = num1 * 2
triplo = num1 * 3
raiz = num1 ** (1/2)

print('O numero {} tem seu dobro como {}' .format(num1, dobro))
print('O numero {} tem seu triplo como {}' .format(num1, triplo))
print('O numero {} tem sua raiz quadrada como {:.2f}' .format(num1, raiz))

#OU SEGUNDA FORMA

n= int(input('Digite um valor: '))

print('O dobro de {} vale {}.' .format(n,(n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.' .format(n, (n*3), n, (n**(1/2))))