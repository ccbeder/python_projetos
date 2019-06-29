#!/usr/bin/python3
def soma(x, y):
    	return x + y
def subtracao(x, y):
	return x - y
def multiplicacao(x, y):
	return x * y
def divisao(x, y):
	return x / y

def menu():
    global escolha
    print("Selecione:")
    escolha = input("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - sair\n>> ")
    if escolha == '1' or escolha == '2' or escolha == '3' or escolha == '4':
        numeros()
    elif escolha == '5':
        exit()
    else:
        print('Opção inválida:')
        menu()

def numeros():
    global num1, num2
    try:
        num1 = float(input("Digite o primeiro número:\n"))
        num2 = float(input("Digite o segundo número:\n"))
    except:
        print('Não é um numero válido')
        numeros()

# Retornar ao inicio
menu()

if escolha == '1':
	print("Resultado: ", soma(num1, num2))
elif escolha == '2':
	print("Resultado: ", subtracao(num1, num2))
elif escolha == '3':
	print("Resultado: ", multiplicacao(num1, num2))
elif escolha == '4':
    try:
	    print("Resultado: ", divisao(num1, num2))
    except ZeroDivisionError as msg:
        print('Opção inválida "valor=zero"'), msg