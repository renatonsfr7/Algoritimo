# valor = int(input("digite um valor:"))
#
# if valor >0:
#      print("Positivo")
#
# else:
#     print("Negativo")

#2-Faça um Programa que peça dois números e imprima o maior deles.
# a = int(input("Digite um números:"))
# b = int(input("Digite outro número:"))
# if a >b:
#     print("Este é o maior:", a)
#
# else:
#     print("Este é maior:", b)

#3-Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
# a = int(input("A:"))
# b = int(input('B:'))
# c = int(input("C:"))
#
# valor = a + b
#
# if valor <c:
#     print("Este valor é menor que C:")
# else:
#     print("Este valor é maior que C:",)

#4-Faça um Programa que verifique o sexo de uma pessoa. O usuário deve informar ‘F’ ou ‘M’ e o programa deve escrever “Feminino” ou “Masculino”, conforme a letra digitada.
# sexo = input("Digite o seu sexo:")
#
# if sexo == "m" :
#     print("Maculino")
#
# else:
#     sexo == "f"
#     print("Feminino")

#5-Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).
# valor = int(input("Digite um número inteiro:"))
#
# if valor %2==0:
#     print("Par")
# else:
#     print("Impar")

#6-Faça um algoritmo que peça um número e se ele for par some 5, se não, some 8.
# valor = int(input("Digite um número:"))
#
# if valor %2==0:
#     print(valor + 5)
#
# else:
#     print(valor + 8)

#7-Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100). Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.
# trabalho = int(input("Nota do trabalho:"))
# prova = int(input("Nota da prova:"))
#
# nota=(trabalho + prova)/2
#
# if nota >=60:
#     print("Aprovado")
#
# else:
#     print("Reprovado")

#8-Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela somente o maior deles.
a = int(input("Valor A:"))
b = int(input("Valor B:"))
c = int(input("Valor C:"))

if a > b and c:
    print("O maior é A")

elif b > a and c:
    print("O maior é B")

elif c > a and b:
    print("O maior é C")
