import time
import random
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        menores = [x for x in arr[1:] if x <= pivot]
        maiores = [x for x in arr[1:] if x > pivot]
        return quicksort(menores) + [pivot] + quicksort(maiores)

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numero_de_testes = 20
min_tamanho = 100
max_tamanho = 200
tamanhos_lista = sorted(random.sample(range(min_tamanho, max_tamanho + 1), numero_de_testes))

velocidades_q = []
velocidades_b = []

for tamanho in tamanhos_lista:
    lista_original = random.sample(range(1, tamanho * 2), tamanho)

    lista_para_quicksort = lista_original.copy()
    start_time_q = time.perf_counter()
    quicksort(lista_para_quicksort)
    end_time_q = time.perf_counter()
    tempo_s_q = end_time_q - start_time_q
    if tempo_s_q > 0:
        velocidades_q.append(tamanho / tempo_s_q)
    else:
        velocidades_q.append(float('inf'))

    lista_para_bubble = lista_original.copy()
    start_time_b = time.perf_counter()
    bubble_sort(lista_para_bubble)
    end_time_b = time.perf_counter()
    tempo_s_b = end_time_b - start_time_b
    if tempo_s_b > 0:
        velocidades_b.append(tamanho / tempo_s_b)
    else:
        velocidades_b.append(float('inf'))


plt.figure(figsize=(10, 6))
plt.plot(tamanhos_lista, velocidades_q, label='Quicksort', marker='o', linestyle='-', color='skyblue')
plt.plot(tamanhos_lista, velocidades_b, label='Bubble Sort', marker='x', linestyle='--', color='salmon')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Velocidade (elementos por segundo)')
plt.title('Comparação de Velocidade de Ordenação')
plt.yscale('log')
plt.legend()
plt.grid(True, which="both", ls="--", c='0.7')
plt.show()