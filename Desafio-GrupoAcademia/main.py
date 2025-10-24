from string import ascii_letters
import time

# palavra = input("Digite a palavra: ")
with open('shrek.txt', 'r') as arquivo:
    palavra = arquivo.read() # Lê todo o conteúdo
    palavra = palavra.replace('\n\n', '\n')

def conta_consoante_vogais_qtd(palavra):
    start = time.time()
    consoantes = set(ascii_letters) - set('aeiouâãáàéíìèúó')
    vogais = set('aeiouâãáàéíìèúó')
    soma_c = 0
    soma_v = 0
    soma = 0
    for c in palavra.lower():
        if c != " " and c != "\n":
            if c in consoantes:
                soma_c += 1
            elif c in vogais:
                soma_v += 1
        elif c == " " or c == "\n":
            soma += 1
    fim = time.time()
    print(fim-start)
    return soma_c, soma_v, soma


print(conta_consoante_vogais_qtd(palavra))
