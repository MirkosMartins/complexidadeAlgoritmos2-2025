def quicksort(lista):
    # Caso base: lista com 0 ou 1 elemento já está ordenada
    if len(lista) <= 1:
        return lista
    
    # Escolhe o pivô (aqui usamos o primeiro elemento)
    pivo = lista[0]
    
    # Particiona a lista em menores, iguais e maiores que o pivô
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]
    
    # Recursivamente ordena menores e maiores
    return quicksort(menores) + [pivo] + quicksort(maiores)

# Exemplo de uso:
valores = [10, 5, 8, 1, 7, 3, 2]
print("Lista original:", valores)
print("Lista ordenada:", quicksort(valores))
