#include <stdio.h>

#define TAMANHO_LISTA 5  // aloca memoria (atribuicao)


int main() {
    int lista1[TAMANHO_LISTA] = {1, 2, 3, 4, 5};  // atribuicao valores
    int lista2[TAMANHO_LISTA] = {6, 7, 8, 9, 10}; // atribuicao valores
    int resultado[TAMANHO_LISTA];  // atribuicao
    
    
    multiplicarListas(lista1, lista2, resultado, TAMANHO_LISTA); // chama funcao com parametros (atribuicao)
    
    
    printf("Resultado da multiplicação das listas:\n"); // atribuicao
    for (int i = 0; i < TAMANHO_LISTA; i++) {       // loop (comparacao + atribuicao + operacao)
        printf("%d ", resultado[i]);    //atribuicao
    }
    
    return 0;
}

void multiplicarListas(int lista1[], int lista2[], int resultado[], int tamanho) { // parametros (atribuicao)
    for (int i = 0; i < tamanho; i++) {       // loop (comparacao + atribuicao + operacao)
        resultado[i] = lista1[i] * lista2[i];    //operacao matematica
    }
}
