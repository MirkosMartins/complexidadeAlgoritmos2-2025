// Codigo Guilherme

#include <stdio.h>

int main() {
    int i, num1, num2;
    char operacao;

    // ATRIBUIÇÃO:
    // Aqui estamos armazenando valores digitados pelo usuário em variáveis.
    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);

    printf("Digite o segundo numero: ");
    scanf("%d", &num2);

    // LOOP:
    for (i = 0; i < 4; i++) {
        printf("\nEscolha a operacao (+, -, *, /): ");
        scanf(" %c", &operacao); // espaço antes do %c para ignorar enter anterior

        // ✅ CONDICIONAL:
        // Aqui usamos if/else if para decidir qual bloco de código executar.
        if (operacao == '+') {
            // OPERAÇÃO MATEMÁTICA:
            printf("Resultado: %d\n", num1 + num2);
        } 
        else if (operacao == '-') {
            // OPERAÇÃO MATEMÁTICA:
            printf("Resultado: %d\n", num1 - num2);
        } 
        else if (operacao == '*') {
            // OPERAÇÃO MATEMÁTICA:
            printf("Resultado: %d\n", num1 * num2);
        } 
        else if (operacao == '/') {
            // OPERAÇÃO MATEMÁTICA:
            if (num2 != 0) {
                printf("Resultado: %.2f\n", (float)num1 / num2);
            } else {
                printf("Erro: divisao por zero!\n");
            }
        } 
        else {
            // Caso o usuário digite algo inválido.
            printf("Operacao invalida!\n");
        }
    }

    printf("\nPrograma encerrado.\n");
    return 0;
}
