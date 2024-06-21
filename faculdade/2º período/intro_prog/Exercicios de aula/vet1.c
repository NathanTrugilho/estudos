//procurar o elemento no vetor, se estiver, imprime em qual posição do vetor está.
#include <stdio.h>

int main(){

    int n, vet[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}, v = 0;


    printf("Digite o valor a ser analiado: ");
    scanf("%d", &n);

    for(int i = 0; i < (sizeof(vet)/sizeof(vet[0])); i++){

        if (n == vet[i]){

            printf("O valor esta na posicao %d do vetor\n", i);
            v = 1;
        }
    }

    if (v == 0) printf("O valor nao existe no vetor!\n");

    return 0;
}