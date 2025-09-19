import matplotlib.pyplot as plt
import numpy as np

# --- Dados da sua execução ---
algoritmos = ['Quicksort', 'Bubble Sort']
tempos_execucao = [2.1961, 187.7659]  # em milissegundos
metricas_operacao = [3367, 1566127]  # Chamadas Recursivas vs. Trocas
nomes_metricas = ['Chamadas Recursivas', 'Trocas de Elementos']

# --- Gráfico 1: Comparação do Tempo de Execução ---
fig1, ax1 = plt.subplots(figsize=(8, 6))
barras1 = ax1.bar(algoritmos, tempos_execucao, color=['#4CAF50', '#F44336'])

# Adiciona título e rótulos
ax1.set_ylabel('Tempo de Execução (milissegundos)')
ax1.set_title('Comparação de Tempo de Execução: Quicksort vs. Bubble Sort')
ax1.set_ylim(0, max(tempos_execucao) * 1.1) # Margem no topo

# Adiciona os valores no topo das barras
for barra in barras1:
    yval = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2.0, yval, f'{yval:.2f} ms', va='bottom', ha='center')

# --- Gráfico 2: Comparação das Métricas de Operação ---
fig2, ax2 = plt.subplots(figsize=(8, 6))
barras2 = ax2.bar(algoritmos, metricas_operacao, color=['#2196F3', '#FF9800'])

# Usar escala logarítmica para visualizar a enorme diferença
ax2.set_yscale('log')

# Adiciona título e rótulos
ax2.set_ylabel('Número de Operações (Escala Logarítmica)')
ax2.set_title('Comparação de Métricas de Operação')

# Adiciona os valores no topo das barras
for i, barra in enumerate(barras2):
    yval = barra.get_height()
    # Texto formatado com separador de milhar para facilitar a leitura
    ax2.text(barra.get_x() + barra.get_width()/2.0, yval, f'{yval:,}\n({nomes_metricas[i]})', va='bottom', ha='center', fontsize=10)

# --- Exibir os gráficos ---
plt.tight_layout()
plt.show()