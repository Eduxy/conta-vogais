def conta_vogais(digitado):
    
    vogais="aeiouAEIOU"
    contagem_vogais = 0

    for char in digitado:
        if char in vogais:
            contagem_vogais +=1

    return contagem_vogais


continua="1"
while (continua=="1"):
    palavra = input("Digite a palavra: ")
    numero_vogais = conta_vogais(palavra)
    print(f"A palavra {palavra} tem {numero_vogais} vogais.")
    continua = input("Deseja testar outra palavra? (1 para sim, qualquer tecla para sair): ")

else:
    print("Fim da execução.")