#include <stdio.h>

int inverteNumero(int numero, int resto){

    if (numero == 0){

        return resto;
    }
    
    int digito = numero % 10;

    resto = (resto * 10) + digito;

    return inverteNumero(numero / 10, resto);
}

int main() {

    int numero;

    printf("Digite um numero inteiro: ");

    scanf("%d", &numero);

    printf("O numero invertido eh: %d", inverteNumero(numero, 0));

    return 0;

}
