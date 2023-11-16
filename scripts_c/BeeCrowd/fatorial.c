#include <stdio.h>

int main(){

    int N, soma;

    scanf("%d", &N);

    soma = N;

    while (N > 1){
        N --;
        soma = soma * N;
    }

    printf("%d\n",soma);

    return 0;

}