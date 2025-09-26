import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

n = np.random.randint(1, 201)

v1 = np.random.randint(1, 201, size=n, dtype=np.int64)
v2 = np.random.randint(1, 201, size=n, dtype=np.int64)
m1 = np.random.randint(1, 201, size=(n, n), dtype=np.int64)
m2 = np.random.randint(1, 201, size=(n, n), dtype=np.int64)

print("="*50)
print(f"VALOR DE N GERADO: {n}")
print("="*50)

print("\n--- VETORES E MATRIZES GERADOS ---\n")
print(f"Vetor 1 (v1) de tamanho {v1.shape}:\n{v1}\n")
print(f"Vetor 2 (v2) de tamanho {v2.shape}:\n{v2}\n")
print(f"Matriz 1 (m1) de tamanho {m1.shape}:\n{m1}\n")
print(f"Matriz 2 (m2) de tamanho {m2.shape}:\n{m2}\n")

execution_times = []
operation_names = ['Vetor x Vetor', 'Vetor x Matriz', 'Matriz x Matriz']

print("="*50)
print("INICIANDO OPERAÇÕES E MEDINDO O TEMPO")
print("="*50)

print("\n--- 1. Multiplicação: Vetor x Vetor ---\n")
start_time = time.perf_counter()
result_vv = np.dot(v1, v2)
end_time = time.perf_counter()
time_vv = end_time - start_time
execution_times.append(time_vv)
print(f"Resultado (Produto Escalar):\n{result_vv}\n")
print(f"Tempo de execução: {time_vv:.8f} segundos\n")

print("\n--- 2. Multiplicação: Vetor x Matriz ---\n")
start_time = time.perf_counter()
result_vm = np.dot(v1, m1)
end_time = time.perf_counter()
time_vm = end_time - start_time
execution_times.append(time_vm)
print(f"Resultado (Vetor de tamanho {result_vm.shape}):\n{result_vm}\n")
print(f"Tempo de execução: {time_vm:.8f} segundos\n")

print("\n--- 3. Multiplicação: Matriz x Matriz ---\n")
start_time = time.perf_counter()
result_mm = np.dot(m1, m2)
end_time = time.perf_counter()
time_mm = end_time - start_time
execution_times.append(time_mm)
print(f"Resultado (Matriz de tamanho {result_mm.shape}):\n{result_mm}\n")
print(f"Tempo de execução: {time_mm:.8f} segundos\n")

sns.set_theme(style="whitegrid")
fig, axs = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle(f'Análise de Desempenho para N = {n}', fontsize=20)

axs[0, 0].scatter(operation_names, execution_times, color='red', s=150, zorder=3)
axs[0, 0].set_title('Tempo de Execução (Gráfico de Dispersão)', fontsize=14)
axs[0, 0].set_ylabel('Tempo (segundos)')
axs[0, 0].grid(True, which='both', linestyle='--', linewidth=0.5)

if max(execution_times) > 1e-5 and max(execution_times) / min(execution_times) > 100:
    axs[0, 0].set_yscale('log')
    axs[0, 0].set_ylabel('Tempo (segundos) - Escala Log')

bars_time = sns.barplot(x=operation_names, y=execution_times, ax=axs[0, 1], palette='viridis')
axs[0, 1].set_title('Tempo de Execução (Gráfico de Barras)', fontsize=14)
axs[0, 1].set_ylabel('Tempo (segundos)')
for bar in bars_time.patches:
    height = bar.get_height()
    axs[0, 1].text(bar.get_x() + bar.get_width() / 2, height, f'{height:.6f}s', ha='center', va='bottom')

if max(execution_times) > 1e-5 and max(execution_times) / min(execution_times) > 100:
    axs[0, 1].set_yscale('log')
    axs[0, 1].set_ylabel('Tempo (segundos) - Escala Log')

flops_vv = 2 * n
flops_vm = 2 * (n**2)
flops_mm = 2 * (n**3)
complexities = [flops_vv, flops_vm, flops_mm]

bars_flops = sns.barplot(x=operation_names, y=complexities, ax=axs[1, 0], palette='plasma')
axs[1, 0].set_title('Complexidade Computacional (FLOPs Estimados)', fontsize=14)
axs[1, 0].set_ylabel('Número de Operações (Escala Log)')
axs[1, 0].set_yscale('log')
for bar in bars_flops.patches:
    height = bar.get_height()
    axs[1, 0].text(bar.get_x() + bar.get_width() / 2, height, f'{height:,.0f}', ha='center', va='bottom')

mem_vv = v1.nbytes + v2.nbytes
mem_vm = v1.nbytes + m1.nbytes
mem_mm = m1.nbytes + m2.nbytes
memory_usage = [mem_vv, mem_vm, mem_mm]
mem_labels = [f'{usage/1024:.2f} KB' if usage >= 1024 else f'{usage} B' for usage in memory_usage]

bars_mem = sns.barplot(x=operation_names, y=memory_usage, ax=axs[1, 1], palette='magma')
axs[1, 1].set_title('Uso de Memória dos Dados de Entrada', fontsize=14)
axs[1, 1].set_ylabel('Memória (bytes)')
for i, bar in enumerate(bars_mem.patches):
    height = bar.get_height()
    axs[1, 1].text(bar.get_x() + bar.get_width() / 2, height, mem_labels[i], ha='center', va='bottom', fontsize=10)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()