kg= float(input("Digite a quantidade de peso do peixe em kilos: "))
if kg <= 50:
    print("Não pagará a multa")
elif kg> 50:
    excesso = (kg-50)*4
print("O valor do excesso é de: R$", round(excesso,2), " reais")