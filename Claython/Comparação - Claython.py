from random import randint
import time
import matplotlib.pyplot as plt
import numpy as np

def criaListaI(numero):
    lista = []
    for i in range(numero):
        lista.append(100-i)
    return lista

def criaLista(numero):
    lista = []
    for i in range(numero):
        lista.append(randint(1,50))
    return lista

def bubblesort(lista):
    tamanho = len(lista)
    for i in range(tamanho-1):
        for j in range(tamanho-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

tempos_bubble = []
tempos_quick = []

for i in range(1000):
    l_bubble = criaListaI(100+i)
    l_quick = criaLista(100+i)
    
    ini = time.time_ns()
    bubblesort(l_bubble)
    fim = time.time_ns()
    tempos_bubble.append(fim-ini)

    ini = time.time_ns()
    quicksort(l_quick)
    fim = time.time_ns()
    tempos_quick.append(fim-ini)
    
    plt.scatter(i, tempos_bubble[i], color='r')
    plt.scatter(i, tempos_quick[i], color='b')

plt.xlabel('Nr elementos')
plt.ylabel('Tempo exec (ns)')
plt.legend(['Bubble Sort', 'Quick Sort'])
plt.show()