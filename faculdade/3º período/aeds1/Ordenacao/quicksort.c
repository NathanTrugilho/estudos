#include <stdio.h>

void swap(int *vetor, int esq, int dir){

    int troca = vetor[dir];
    vetor[dir] = vetor[esq];
    vetor[esq] = troca;
}

int particao(int *vetor, int esq, int dir){

    int pivo = vetor[(esq + dir)/2];

    while (esq <= dir){
        while(vetor[esq] < pivo) esq++;
        while(vetor[dir] > pivo) dir--; 

        if(esq < dir){
            swap(vetor, esq, dir);
            esq++;
            dir--;
        }
        else break;
    }
    return dir;
}

void quicksort(int *vetor, int esquerda, int direita){

    if(esquerda < direita){
        int pivo = particao(vetor, esquerda, direita);
        quicksort(vetor, esquerda, pivo);
        quicksort(vetor, pivo + 1, direita);
    }
}

void main(){

    int vetor[16] = {122,75,36,1168,57,6,8345,15,287,1,8098,0,422,56,7,2};

    quicksort(vetor, 0, 15);

    for(int i = 0; i < 16; printf("%d ", vetor[i]), i++);

}