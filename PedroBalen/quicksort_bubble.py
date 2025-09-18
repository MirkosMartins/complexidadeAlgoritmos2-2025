

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


contador_bubble_sort = 0

def bubble_sort(lista):
    global contador_bubble_sort
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            contador_bubble_sort += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista_fixa = [42, 8, 15, 23, 4, 16, 88, 52, 34, 7, 99, 29]
print(f"{lista_fixa}\n")

print("--- Executando Quicksort ---")
lista_para_quicksort = lista_fixa.copy()
lista_ordenada_q = quicksort(lista_para_quicksort)
print(f"Lista ordenada: {lista_ordenada_q}")
print(f"O Quicksort foi chamado {contador_quicksort} vezes (chamadas recursivas).\n")


print("--- Executando Bubble Sort ---")
lista_para_bubble = lista_fixa.copy()
lista_ordenada_b = bubble_sort(lista_para_bubble)
print(f"Lista ordenada: {lista_ordenada_b}")
print(f"O Bubble Sort realizou {contador_bubble_sort} comparações.")