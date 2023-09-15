#include <stdio.h>

int main(){

    int n, nv = 1;

    printf("Quantos numeros serao adicionados ao vetor: ");
    scanf("%d", &n);

    int vet[n];

    printf("Digite os numeros (0 < n < 100): \n");

    for(int i = 0; i < n; i++){

        scanf("%d", &nv);

        if(nv < 1 || nv > 99){

            printf("Valor invalido! \n");
            i --;
        }

        else vet[i] = nv;
   
    }

    for(int j = n-1; j >= 0; j--){

        printf("%d ", vet[j]);
    }

    return 0;

}