tanqueGasolina = int(input("Informe a quantidade de gasolina no tanque: "))

horasPercorridas = int(input("Ok, agora informe quantas horas foram precorridas: "))

velocidadeMedia = int(input("Por fim me diga qual era a velocidade média: "))

if (tanqueGasolina < 1 or horasPercorridas < 1 or velocidadeMedia < 1):
    print ("Entre com dados validos!")
else :
    #calculo para descobrir o valor
    kmMedia = velocidadeMedia * horasPercorridas / float(tanqueGasolina)

    print ("\nO consumo médio foi de ", kmMedia, " km percorridos por litro: ")