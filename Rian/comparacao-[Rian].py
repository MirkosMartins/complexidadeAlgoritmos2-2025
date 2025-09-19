import time
import random
import sys

sys.setrecursionlimit(3000)

contador_quicksort = 0

def quicksort(arr):
    global contador_quicksort
    contador_quicksort += 1

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        menores = [x for x in arr[1:] if x <= pivot]
        maiores = [x for x in arr[1:] if x > pivot]
        return quicksort(menores) + [pivot] + quicksort(maiores)

contador_trocas_bubble = 0

def bubble_sort(arr):
    global contador_trocas_bubble
    n = len(arr)
    for i in range(n):
        troca_ocorreu = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                contador_trocas_bubble += 1
                troca_ocorreu = True
        if not troca_ocorreu:
            break
    return arr

tamanho_da_lista = 2500
print(f"--- Comparando Quicksort vs. Bubble Sort ---")
print(f"Tamanho da lista: {tamanho_da_lista} elementos gerados aleatoriamente.\n")
lista_original = random.sample(range(1, 20001), tamanho_da_lista)

lista_para_quicksort = lista_original.copy()
start_time_q = time.perf_counter()
lista_ordenada_q = quicksort(lista_para_quicksort)
end_time_q = time.perf_counter()
tempo_execucao_q_ms = (end_time_q - start_time_q) * 1000

lista_para_bubble = lista_original.copy()
start_time_b = time.perf_counter()
lista_ordenada_b = bubble_sort(lista_para_bubble)
end_time_b = time.perf_counter()
tempo_execucao_b_ms = (end_time_b - start_time_b) * 1000

print("--- Resultados ---")

print("\n[ Quicksort ]")
print(f"Tempo de execução: {tempo_execucao_q_ms:.4f} milissegundos.")
print(f"Métrica (Chamadas Recursivas): {contador_quicksort} chamadas.")

print("\n[ Bubble Sort ]")
print(f"Tempo de execução: {tempo_execucao_b_ms:.4f} milissegundos.")
print(f"Métrica (Trocas de Elementos): {contador_trocas_bubble} trocas.")