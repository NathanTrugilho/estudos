#include <stdio.h>

int buscab(int i, int *vet, int f, int valor){
    int M = (i + f)/2;

    if(vet[M] == valor) return M;

    if (f < i) return -1;

    else if(vet[M] < valor){
        i = M + 1;
        return buscab(i, vet, f, valor);
    }

    else if (vet[M] > valor){
        f = M - 1;
        return buscab(i, vet, f, valor);
    }

}

void main(){

    int vet[20] = {1,2,3,4,5,6,7,7,8,9,10,11,12,13,15,17,18,23,144,925};

    printf("%d", buscab(0, vet, 20, 12));
}