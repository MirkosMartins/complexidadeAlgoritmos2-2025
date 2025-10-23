from string import ascii_letters
import time

palavra = input("Digite a palavra: ")

def conta_consoante_vogais_qtd(palavra):
    start = time.time()
    consoantes = set(ascii_letters) - set('aeiou')
    vogais = set('aeiou')
    soma_c = 0
    soma_v = 0
    soma = 0
    for c in palavra.lower():
        if c != " ":
            if c in consoantes:
                soma_c += 1
            elif c in vogais:
                soma_v += 1
            soma += 1
    fim = time.time()
    print(fim-start)
    return soma_c, soma_v, soma


print(conta_consoante_vogais_qtd(palavra))