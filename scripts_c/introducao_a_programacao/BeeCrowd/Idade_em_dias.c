#include <stdio.h>

int main (){

    int idade_em_dias, ano = 0, mes = 0;

    scanf("%d", &idade_em_dias);

    while (idade_em_dias >= 365){
        ano ++;
        idade_em_dias = idade_em_dias - 365;
    }
    
    while (idade_em_dias >= 30){
        mes ++;
        idade_em_dias = idade_em_dias - 30;
    }
    
    printf("%d" " ano(s)\n%d" " mes(es)\n%d" " dia(s)\n", ano, mes, idade_em_dias);

    return 0;
}