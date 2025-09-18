def quicksort(lista, a):
    if len(lista) <= 1:
        return lista  # Condição de parada: lista já está ordenada
    pivot = lista[0]  # Escolhe o primeiro elemento como pivô
    print(a , "quick")
    menores = [x for x in lista[1:] if x <= pivot] # Elementos menores que o pivô
    maiores = [x for x in lista[1:] if x > pivot] # Elementos maiores que o pivô

    # Aplica o quicksort recursivamente nas sublistas e concatena
    return quicksort(menores, a + 1) + [pivot] + quicksort(maiores, a + 1)

# Exemplo de uso:
minha_lista = [ 11 , 10 ,9, 8, 7 , 6, 5, 4, 3, 2, 1]
lista_ordenada = quicksort(minha_lista, 1)
print(f"A lista original era: {minha_lista}")
print(f"A lista ordenada com Quicksort é: {lista_ordenada}")



def bubble_sort(lista, a):
    # Itera através da lista várias vezes (passagens)
    for passnum in range(len(lista) - 1, 0, -1):
        a= a + 1
        print (a)
        # Percorre a lista para fazer comparações e trocas
        for i in range(passnum):
            # Compara um elemento com o próximo
            if lista[i] > lista[i+1]:
                # Troca os elementos se estiverem fora de ordem
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return lista


print(f"Lista original: {minha_lista}")
# Chama a função bubble_sort para ordenar a lista
bubble_sort(minha_lista, 0)

# Imprime a lista ordenada
print(f"Lista ordenada: {minha_lista}")
