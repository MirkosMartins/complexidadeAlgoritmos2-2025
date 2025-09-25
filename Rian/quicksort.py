import random
import matplotlib.pyplot as plt

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



lista = [random.randint(0, 50) for _ in range(12)]

print("Lista original:", lista)
resultado = quicksort(lista)
print("Lista ordenada:", resultado)
print("Número de chamadas recursivas:", contador)



plt.figure(figsize=(10,5))


plt.subplot(1,2,1)
plt.bar(range(len(lista)), lista, color="skyblue")
plt.title("Lista Original")


plt.subplot(1,2,2)
plt.bar(range(len(resultado)), resultado, color="lightgreen")
plt.title("Lista Ordenada")

plt.suptitle(f"Quicksort - Chamadas Recursivas: {contador}")
plt.tight_layout()
plt.show()
