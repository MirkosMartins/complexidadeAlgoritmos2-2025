import time

def analisar_frase():
    frase = input("Digite uma frase: ")    
    inicioT = time.time()
    palavras = frase.split()
    qtd_palavras = len(palavras)

    vogais = "aeiouAEIOU"

    qtd_vogais = 0
    qtd_consoantes = 0

    for letra in frase:
        if letra.isalpha(): #só letras
            if letra in vogais:
                qtd_vogais += 1
            else:
                qtd_consoantes += 1
    fimT = time.time()
    tempo_exec = fimT - inicioT
    print(f"Tempo de execução das contagens: {tempo_exec:6f}")
    return qtd_palavras, qtd_vogais, qtd_consoantes

def main():
    palavras, vogais, consoantes = analisar_frase()

    print(f"Quantidade de palavras: {palavras}")
    print(f"Quantidade de vogais: {vogais}")
    print(f"Quantidade de consoantes: {consoantes}")

if __name__ == "__main__":
    main()
