import os
import time

def analisar_arquivo(nome_arquivo):
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Por favor, crie este arquivo no mesmo diretório do script.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None

    VOGAIS = "aeiouáéíóúâêôãõàü"
    CONSOANTES = "bcdfghjklmnpqrstvwxyzç"
    
    cont_vogais = 0
    cont_consoantes = 0
    
    for char in conteudo:
        char_lower = char.lower()
        
        if char_lower in VOGAIS:
            cont_vogais += 1
        elif char_lower in CONSOANTES:
            cont_consoantes += 1

    palavras = conteudo.split()
    total_palavras = len(palavras)

    return cont_vogais, cont_consoantes, total_palavras


nome_do_seu_arquivo = "texto.txt"

inicio = time.perf_counter()

resultados = analisar_arquivo(nome_do_seu_arquivo)

fim = time.perf_counter()

duracao_s = fim - inicio

if resultados:
    vogais, consoantes, palavras = resultados
    
    print(f"Total de Vogais: {vogais}")
    print(f"Total de Consoantes: {consoantes}")
    print(f"Total de Palavras: {palavras}")
    print(f"Tempo de execução: {duracao_s:.6f} s")
