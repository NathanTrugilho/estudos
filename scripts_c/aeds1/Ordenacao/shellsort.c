#include <stdio.h>

void shellSort(int vetor[], int tamanho) {
    int intervalo, i, j, temp;
    for(intervalo = tamanho/2; intervalo > 0; intervalo /= 2) {
        for(i = intervalo; i < tamanho; i++) {
            temp = vetor[i];
            for(j = i; j >= intervalo && vetor[j-intervalo] > temp; j -= intervalo) {
                vetor[j] = vetor[j-intervalo];
            }

            vetor[j] = temp;
        }
    }
}

int main() {
    int vetor[20] = {11, 8, 13, 2, 9, 5, 16, 20, 7, 12, 1, 6, 18, 15, 3, 14, 4, 19, 17, 10};
    int tamanho = 20;
    shellSort(vetor, tamanho);
    for(int k = 0; k < tamanho; k++) {
        printf("%d ", vetor[k]);
    }
    printf("\n");
    return 0;
}
