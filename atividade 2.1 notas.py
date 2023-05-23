n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota:  "))
n3 = float(input("Digite sua terceira nota:  "))
n4 = float(input("Digite sua quarta nota:  "))
mediaAritc = (n1+n2+n3+n4)/4
print("Sua média é: ", round(mediaAritc))
if mediaAritc == 0 in mediaAritc <=3.9:
    print("Em processo de Aprendizagem (Reprovado)")
elif mediaAritc == 4 in mediaAritc <= 8:
    print("Recuperação")
else:
    print("Aprovado!")