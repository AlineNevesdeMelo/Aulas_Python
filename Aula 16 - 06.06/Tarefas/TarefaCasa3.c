//Crie um vetor com 5 elementos inteiros e conte quantos elementos são pares.

#include <stdio.h> //Esta biblioteca é necessária para usar a função 'printf' que permite imprimir no console.

int main() {
    // Criação do vetor com 5 elementos inteiros
    int vetor [5] = {3, 8, 11, 20, 7}; //Declaração do vetor
    int contador_pares = 0; //Declaração do contador(variável)

    // Loop para imprimir cada elemento separadamente
    for(int i = 0; i < 5; i++) { //Loop para analisar cada elemento do vetor
        if(vetor[i] % 2 == 0) { //Condicional para verificação do elementos pares
            contador_pares++; // ++ é o incremento que vai fazer adicionar uma unidade ao contador(variável).
        }
    }
    printf("Quantidade de elementos pares: %d\n", contador_pares); //Impressão do resultado
    // %: É um caractere especial que indica o início de um especificador de formato.
    // d: Especifica que o valor a ser inserido na string de formato é um número inteiro (decimal). O d vem de "decimal".
    // Quando \n é encontrado, o cursor do terminal ou console se move para o início da próxima linha.
}