import time



with open('arquivo.txt', 'r') as arquivo:
    texto = arquivo.read()

def contar_vogais_consoantes(texto):
    vogais = "aeiou"
    texto = texto.lower()
    texto = texto.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    palavras = texto.split()
    numero_de_palavras = len(palavras)
    num_vogais = 0
    num_consoantes = 0
    inicio = time.time()
    for char in texto:
            if char in vogais:
                num_vogais += 1
            else:
                num_consoantes += 1
    fim = time.time()
    tempo = fim - inicio
    return num_vogais, num_consoantes, numero_de_palavras, tempo

print(contar_vogais_consoantes(texto))



