#include <stdio.h>; //Esta biblioteca é necessária para usar a função 'printf' que permite imprimir no console.

int main() {
    // Criação do vetor com 5 elementos inteiros
    int vetor[5] = {10, 20, 30, 40, 50};
    
    // Loop para imprimir cada elemento separadamente
    for(int i = 0; i < 5; i++) {
        printf("%d\n", vetor[i]);
    }

    return 0; //A função main retorna 0 indicando que o programa terminou com sucesso.
}
