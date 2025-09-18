import random

contador = 0  

def quicksort(arr):
    global contador
    contador += 1  
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] 
        menores = [x for x in arr[1:] if x <= pivot]
        maiores = [x for x in arr[1:] if x > pivot]
        return quicksort(menores) + [pivot] + quicksort(maiores)


# Gera 12 números aleatórios entre 0 e 50
lista = [random.randint(0, 50) for _ in range(12)]

print("Lista original:", lista)
resultado = quicksort(lista)
print("Lista ordenada:", resultado)
print("Número de chamadas recursivas:", contador)
