def quicksort(arr):
    chamadas = 0
    def _quicksort_recursivo(arr):
        nonlocal chamadas
        chamadas += 1
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            
            return _quicksort_recursivo(left) + middle + _quicksort_recursivo(right)
    
    sorted_arr = _quicksort_recursivo(arr)
    print(f"O quicksort foi chamado {chamadas} vezes.")
    return sorted_arr

data = [12,11,10,9,8,7,6,5,4,3,2,1]
print("Desordenado:", data)
sorted_data = quicksort(data)
print("Ordenado:", sorted_data)


def bubble_sort_com_contador(arr):
    n = len(arr)
    iteracoes = 0

    for i in range(n):
        iteracoes += 1
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr, iteracoes

data = [12,11,10,9,8,7,6,5,4,3,2,1]
print("Lista original:", data)

# Chama a função para ordenar e contar
lista_ordenada, num_iteracoes = bubble_sort_com_contador(data)

print("Lista ordenada:", lista_ordenada)
print(f"O loop externo do Bubble Sort foi executado {num_iteracoes} vezes.")