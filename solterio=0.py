solteiro=0
casado=0
divorciado=0
idade=0
masculino=0
feminino=0
habitantes=0
maisvelhosolteiro = 0
maisvelhocasado = 0
maisvelhodivorciado = 0
maisnovosolteiro = 999
maisnovocasado = 999
maisnovodivorciado =999
solteiromasculino=0
solteirofeminino=0
casadomasculino=0
casadofeminino=0
divorciadomasculino=0
divorciadofeminino=0
idadedosparticipantes=0




while (True):
    statuscivil=(input("digite seu status civil: 1-Solteiro, 2-casado, 3-divorciado"))
    idadedosparticipantes=int(input("digite sua idade"))
    sexo=(input("digite seu sexo M-masculino, F-feminino"))

    if statuscivil=="1":
        if sexo=="M":
            solteiromasculino +=1
            solteiro +=1
            habitantes +=1
            if idadedosparticipantes > maisvelhosolteiro:
                maisvelhosolteiro=idadedosparticipantes
            if idadedosparticipantes < maisnovosolteiro:
                maisnovosolteiro=idadedosparticipantes
        if sexo=="F":
            solteirofeminino +=1
            solteiro +=1
            habitantes +=1
            if idadedosparticipantes > maisvelhosolteiro:
                maisvelhosolteiro=idadedosparticipantes
            if idadedosparticipantes < maisnovosolteiro:
                maisnovosolteiro=idadedosparticipantes
    if statuscivil=="2":
        if sexo=="M":
            casadomasculino +=1
            casado +=1
            habitantes +=1
            if idadedosparticipantes > maisvelhocasado:
                maisvelhocasado=idadedosparticipantes
            if idadedosparticipantes < maisnovocasado:
                maisnovocasado=idadedosparticipantes
        if sexo=="F":
            casadofeminino +=1
            casado +=1
            habitantes +=1
            if idadedosparticipantes > maisvelhocasado:
                maisvelhocasado=idadedosparticipantes
            if idadedosparticipantes < maisnovocasado:
                maisnovocasado=idadedosparticipantes
    if statuscivil=="3":
        if sexo=="M":
            divorciadomasculino +=1
            divorciado +=1
            habitantes +=1
            if idadedosparticipantes > maisvelhodivorciado:
                maisvelhodivorciado=idadedosparticipantes
            if idadedosparticipantes < maisnovodivorciado:
                maisnovodivorciado=idadedosparticipantes
        if sexo=="F":
            divorciadofeminino +=1
            divorciado +=1
            habitantes +=1
            if (idade> maisvelhodivorciado):
                maisvelhodivorciado=idade
            if (idade < maisnovodivorciado):
                maisnovodivorciado=idade
            if idadedosparticipantes > maisvelhodivorciado:
                maisvelhodivorciado=idadedosparticipantes
            if idadedosparticipantes < maisnovodivorciado:
                maisnovodivorciado=idadedosparticipantes



    continua = int(input("Deseja continuar? (1-Sim 2-Não): "))
    if continua == 2:
        break


print(f"Porcentagem de Solteiros: {int(solteiro/habitantes*100)}%")
print(f"Porcentagem de Casados: {int(casado/habitantes*100)}%")
print(f"Porcentagem de Divorciados: {int(divorciado/habitantes*100)}%")
print(f"Idade do mais velho solteiro: {maisvelhosolteiro}")
print(f"Idade do mais velho casado: {maisvelhocasado}")
print(f"Idade do mais velho divorciado: {maisvelhodivorciado}")
print(f"Idade do mais novo solteiro: {maisnovosolteiro}")
print(f"Idade do mais novo casado: {maisnovocasado}")
print(f"Idade do mais novo divorciado: {maisnovodivorciado}")
print(f"Homens solteiros: {solteiromasculino}")
print(f"Mulheres solteiras: {solteirofeminino}")
print(f"Homens casados: {casadomasculino}")
print(f"Mulheres casadas: {casadofeminino}")
print(f"Homens divorciados: {divorciadomasculino}")
print(f"Mulheres divorciadas: {divorciadofeminino}")


