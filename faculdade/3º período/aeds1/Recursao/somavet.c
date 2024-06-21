#include <stdio.h>

/*void soma(int *vet, int *res, int n){

    if (n < 0) return;

    *res = *res + vet[n];
    soma(vet, res, n-1);

}*/

int somavet(int *vet, int len)
{
    if(len == 0) return vet[0];

    return vet[len] + somavet(vet, len - 1);
}

int main(){

    //int res = 0;
    int vet[5] = {1,2,3,4,5};

    //soma(vet, &res, 4);
    
    printf("%d", somavet(vet, 4));

    //printf("%d", res);

    return 0;
}