# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

opcao = -1
contas = False
while (opcao != 0):
	print("\n******************* Python Calculator *******************\n\n\n")
	opcao = int(input('1: adição \n2: subtração \n3: multiplicação \n4: divisão \n\n0: para sair \n\n'))
	if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
		contas = True
	elif opcao == 0:
		print('\n\nObrigado por utilizar a calculadora\n\n')
	else:
		print('\n\nOpção inválida!\n\n')

	while (contas):
		if opcao == 1:
			num1 = float(input('\nDigite o primeiro número: '))
			num2 = float(input('\nDigite o segundo número: '))
			print('\n\nA adição de %r + %r é = %r \n\n' %(num1,num2,num1+num2))
			contas = False

		elif opcao == 2:
			num1 = float(input('\nDigite o primeiro número: '))
			num2 = float(input('\nDigite o segundo número: '))
			print('\n\nA subtração de %r - %r é = %r \n\n' %(num1,num2,num1-num2))
			contas = False

		elif opcao == 3:
			num1 = float(input('\nDigite o primeiro número: '))
			num2 = float(input('\nDigite o segundo número: '))
			print('\n\nA multiplicação de %r * %r é = %r \n\n' %(num1,num2,num1*num2))
			contas = False

		elif opcao == 4:
			num1 = float(input('\nDigite o primeiro número: '))
			num2 = float(input('\nDigite o segundo número: '))
			print('\n\nA divisão de %r / %r é = %r \n\n' %(num1,num2,num1/num2))
			contas = False