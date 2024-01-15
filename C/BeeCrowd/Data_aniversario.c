#include <stdio.h>

int main(){

    int dia, mes, ano;
    
    puts("insira o dia: ");
    scanf("%d", &dia);
    
    puts("insira o mes: ");
    scanf("%d", &mes);

    puts("insira o ano ");
    scanf("%d", &ano);

    printf("voce nasceu em: %02d/%02d/%2d\n", dia, mes, ano);
    return 0;
}