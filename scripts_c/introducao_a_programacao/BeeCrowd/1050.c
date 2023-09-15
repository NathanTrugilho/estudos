#include <stdio.h>

int main(){

    int N;
    
    scanf("%d", &N);

    if (N == 61){
        printf("Brasilia\n");
    }   
    if (N == 71){
        printf("Salvador\n");
    }   
    if (N == 11){
        printf("Sao Paulo\n");
    }   
    if (N == 21){
        printf("Rio de Janeiro\n");
    }   
    if (N == 32){
        printf("Juiz de Fora\n");
    }   
    if (N == 19){
        printf("Campinas\n");
    }   
    if (N == 27){
        printf("Vitoria\n");
    }   
    if (N == 31){
        printf("Belo Horizonte\n");
    }   
    if (N != 61 &&  N != 71 && N != 11 && N != 21 && N != 32 && N != 19 && N != 27 && N != 31){
        printf("DDD nao cadastrado\n");
    }   
    return 0;   
}