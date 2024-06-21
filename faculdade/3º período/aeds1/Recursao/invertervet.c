#include <stdio.h>

void inverte(int tam, int *vet, int *i, int *troca){

    if (*i >= tam){
        return;
    }

    *troca = vet[*i];
    vet[*i] = vet[tam];
    vet[tam] = *troca;
    ++*i;
    return inverte(tam - 1, vet, i, troca);
}

int main(){

    int tam = 9, i = 0, troca;
    int vet[10] = {0,1,2,3,4,4,4,7,8,9};

    for(int j = 0; j <= tam; j++){
        printf("%d",vet[j]);
    }

    inverte(tam, vet, &i, &troca);
    printf("\n");

    for(int j = 0; j <= tam; j++){
        printf("%d",vet[j]);
    }

    return 0;
}