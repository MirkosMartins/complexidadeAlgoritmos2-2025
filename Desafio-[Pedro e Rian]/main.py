import os
import time

VOGAIS = "aeiouáéíóúâêôãõàü"
CONSOANTES = "bcdfghjklmnpqrstvwxyzç"

def ler_conteudo_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return f.read()
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None

def analisar_caracteres(conteudo):
    cont_vogais = 0
    cont_consoantes = 0
    
    for char in conteudo:
        char_lower = char.lower()
        if char_lower in VOGAIS:
            cont_vogais += 1
        elif char_lower in CONSOANTES:
            cont_consoantes += 1
            
    return cont_vogais, cont_consoantes

def contar_palavras(conteudo):
    palavras = conteudo.split()
    return len(palavras)

def imprimir_resultados(vogais, consoantes, palavras, duracao_ms):
    print(f"Total de Vogais: {vogais}")
    print(f"Total de Consoantes: {consoantes}")
    print(f"Total de Palavras: {palavras}")
    print(f"Tempo de execução: {duracao_ms:.4f} ms")

def main():
    nome_arquivo = "texto.txt"
    
    inicio = time.perf_counter()
    
    conteudo = ler_conteudo_arquivo(nome_arquivo)
    
    if conteudo is None:
        return

    vogais, consoantes = analisar_caracteres(conteudo)
    palavras = contar_palavras(conteudo)
    
    fim = time.perf_counter()
    
    duracao_ms = (fim - inicio) * 1000

    imprimir_resultados(vogais, consoantes, palavras, duracao_ms)

if __name__ == "__main__":
    main()
