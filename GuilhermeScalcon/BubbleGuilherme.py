def bubblesort(lista):
    n = len(lista)
    # Passa por toda a lista
    for i in range(n):
        # Últimos i elementos já estão no lugar correto
        for j in range(0, n - i - 1):
            # Troca se o elemento atual é maior que o próximo
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Exemplo de uso
valores = [10, 5, 8, 1, 7, 3, 4, 2, 9, 0, 11, 12]
print("Lista original:", valores)
print("Lista ordenada:", bubblesort(valores))
