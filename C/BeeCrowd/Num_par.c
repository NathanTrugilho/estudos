#include <stdio.h>

int main(){
    int numero;

    printf("Digite o numero a ser verificado: \n");
    scanf("%d", &numero);

    if((numero%2)==0){
        printf("O numero e par!");
    }
    
    else{
        printf("numero e impar!");
    }

    return 0;
}