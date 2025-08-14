#include <stdio.h>

int main() {
    int num1 = 10; // Atribuição
    int num2 = 5; // Atribuição
    int soma, subtracao, multiplicacao, divisao;

    soma = num1 + num2; // Operação
    subtracao = num1 - num2; // Operação
    multiplicacao = num1 * num2; // Operação
    divisao = num1 / num2; // Operação

    printf("Soma: %d\n", soma); // Atribuição
    printf("Subtração: %d\n", subtracao); // Atribuição
    printf("Multiplicação: %d\n", multiplicacao); // Atribuição
    printf("Divisão (inteira): %d\n", divisao); // Atribuição

    if (num1 > num2) { // Comparação
        printf("%d é maior que %d\n", num1, num2); // Atribuição
    } else if (num1 < num2) {// Comparação
        printf("%d é menor que %d\n", num1, num2); // Atribuição
    } else {
        printf("%d é igual a %d\n", num1, num2); // Atribuição
    }

    if (num1 != 0) { // Comparação
        printf("%d é diferente de 0\n", num1); // Atribuição
    }

    return 0;
}