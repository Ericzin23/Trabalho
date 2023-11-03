def convertAvaliacao(avaliacao):
    if (avaliacao == 1):
        return "Ótimo"
    if (avaliacao == 2):
        return "Bom"
    if (avaliacao == 3):
        return "Regular"
    if (avaliacao == 4):
        return "Péssimo"



quantidade = 0
quantidadeOtimo = 0
quantidadeBom = 0
quantidadeRegular = 0
quantidadePessimo = 0
idadeMaisVelho = 0
avaliacaoMaisVelho = 0
idadeMaisNovo = 0
avaliacaoMaisNovo = 0

while (True):
    avaliacao = int(input("Informe sua avaliação (1-Ótimo 2-Bom 3-Regular 4-Péssimo): "))
    idade = int(input("Informe sua idade:"))

    quantidade += 1

    if avaliacao == 1:
        quantidadeOtimo += 1
    if avaliacao == 2:
        quantidadeBom += 1
    if avaliacao == 3:
        quantidadeRegular += 1
    if avaliacao == 4:
        quantidadePessimo += 1

    if (idade > idadeMaisVelho):
        idadeMaisVelho = idade
        avaliacaoMaisVelho = avaliacao

    if (idade < idadeMaisNovo) or (idadeMaisNovo == 0):
        idadeMaisNovo = idade
        avaliacaoMaisNovo = avaliacao

    continua = int(input("Deseja continuar? (1-Sim 2-Não): "))
    if continua == 2:
        break

print("Total de respondentes: ", quantidade)
print("Total de resposta Ótimo: ", quantidadeOtimo)
print("Total de resposta Bom: ", quantidadeBom)
print("Total de resposta Regular: ", quantidadeRegular)
print("Total de resposta Péssimo: ", quantidadePessimo)
print("O respondente mais velho tem ", idadeMaisVelho)
print("A resposta do respondente mais velho foi: ", convertAvaliacao(avaliacaoMaisVelho))
print("O respondente mais novo tem ", idadeMaisNovo)
print("A resposta do respondente mais novo foi: ", convertAvaliacao(avaliacaoMaisNovo))


elvedorAdemanha=0
elvedorBdemanha=0
elvedorCdemanha=0
elvedorAdetarde=0
elvedorBdetarde=0
elvedorCdetarde=0
elvedorAdenoite=0
elvedorBdenoite=0
elvedorCdenoite=0

while(True):
    elevador=input("O elevador é A,B ou C?")
    periodo=input("No periodo M=matutino, V=vespertino ou N=noturno")

    if elevador=="A":
        if periodo=="M":
            elvedorAdemanha +=1
        if periodo=="V":
            elvedorAdetarde +=1
        if periodo=="N":
            elvedorAdenoite +=1
    
    if elevador=="B":
        if periodo=="M":
            elvedorBdemanha +=1
        if periodo=="V":
            elvedorBdetarde +=1
        if periodo=="N":
            elvedorBdenoite +=1
    
    if elevador=="C":
        if periodo=="M":
            elvedorCdemanha +=1
        if periodo=="V":
            elvedorCdetarde +=1
        if periodo=="N":
            elvedorCdenoite +=1
    continua = int(input("Deseja continuar? (1-Sim 2-Não): "))
    if continua == 2:
        break

maior=max((elvedorAdemanha,"A","Manha"),(elvedorAdetarde, "A", "tarde"), (elvedorAdenoite, "A", "noite"), (elvedorBdemanha, "B", "manha"), (elvedorBdetarde, "B", "tarde"),
(elvedorBdenoite, "B", "noite"), (elvedorCdemanha, "C", "manha"), (elvedorCdetarde, "C", "tarde"), (elvedorCdenoite, "C", "noite"))
menorperiodo=min((elvedorAdemanha+elvedorBdemanha+elvedorCdemanha, "manha"), (elvedorAdetarde+elvedorBdetarde+elvedorCdetarde, "tarde"), (elvedorAdenoite+elvedorBdenoite+elvedorCdenoite, "noite"))
maiorperiodo=max((elvedorAdemanha+elvedorBdemanha+elvedorCdemanha, "manha"), (elvedorAdetarde+elvedorBdetarde+elvedorCdetarde, "tarde"), (elvedorAdenoite+elvedorBdenoite+elvedorCdenoite, "noite"))
print(f"o elevador mais ultilizado é o:  {maior[1]}, no periodo: {maior[2]}")
print(f"o Periodo menos ultizado é: {menorperiodo[1]},o periodo mais ultizado é: {maiorperiodo[1]}")








