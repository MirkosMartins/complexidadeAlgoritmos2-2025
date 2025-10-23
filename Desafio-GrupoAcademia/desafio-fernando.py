import time 

def analisar_frase_simultaneamente(frase):
    vogais = "aeiouáàâãéêíóôõúüAEIOUÁÀÂÃEÉÊÍÓÔÕÚÜ"
    
    num_vogais = 0
    num_consoantes = 0
    num_palavras = 0

    dentro_da_palavra = False
    
    for char in frase:
        if char.isalpha():
            if char in vogais:
                num_vogais += 1
            else:
                num_consoantes += 1
            if not dentro_da_palavra:
                dentro_da_palavra = True
                num_palavras += 1
        else:
            dentro_da_palavra = False
            
    return num_palavras, num_vogais, num_consoantes

frase_usuario = input("Digite uma frase para analisar: ")
inicio_tempo = time.perf_counter()
palavras, vogais, consoantes = analisar_frase_simultaneamente(frase_usuario)
fim_tempo = time.perf_counter()
tempo_total = fim_tempo - inicio_tempo

print("\n--- Análise da Frase (Simultânea) ---")
print(f"Frase: '{frase_usuario}'")
print(f"Número de palavras: {palavras}")
print(f"Número de vogais: {vogais}")
print(f"Número de consoantes: {consoantes}")
print("---")
print(f"Tempo de execução da análise: {tempo_total:.9f} segundos")