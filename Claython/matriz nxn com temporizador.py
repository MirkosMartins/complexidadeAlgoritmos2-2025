import numpy as np
import time
import matplotlib.pyplot as plt

# Função para multiplicar duas matrizes manualmente
def multiply_matrices(matrix1, matrix2):
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    cols_matrix2 = len(matrix2[0])

    # Cria uma matriz de resultado com zeros
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # Realiza a multiplicação manualmente
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Lista de tamanhos de matrizes para testar (1x1 até 500x500)
matrix_sizes = range(1, 501)
execution_times = []

# Inicia a medição do tempo total
total_start_time = time.time()

# Mede o tempo de execução para cada tamanho de matriz
for size in matrix_sizes:
    # Gera duas matrizes quadradas do tamanho atual com números aleatórios entre 0 e 50
    matrix1 = np.random.randint(0, 51, size=(size, size)).tolist()
    matrix2 = np.random.randint(0, 51, size=(size, size)).tolist()

    # Mede o tempo de multiplicação
    start_time = time.time()
    result = multiply_matrices(matrix1, matrix2)
    end_time = time.time()

    # Calcula o tempo gasto
    elapsed_time = end_time - start_time
    execution_times.append(elapsed_time)
    print(f"Tamanho da matriz: {size}x{size}, Tempo: {elapsed_time:.6f} segundos")

# Finaliza a medição do tempo total
total_end_time = time.time()
total_elapsed_time = total_end_time - total_start_time

# Gera o gráfico de tempo x tamanho da matriz
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes, execution_times, marker='o', linestyle='-', color='b', label='Tempo de execução')
plt.title('Tempo de Execução x Tamanho da Matriz')
plt.xlabel('Tamanho da Matriz (NxN)')
plt.ylabel('Tempo de Execução (segundos)')
plt.grid(True)
plt.legend()
plt.show()

# Exibe o tempo total de execução
print(f"Tempo total de execução: {total_elapsed_time:.6f} segundos")