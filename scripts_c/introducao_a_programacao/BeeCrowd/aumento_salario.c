#include <stdio.h>

int main(){

    float salario, novo, ajuste, reajuste;
    char porc;

    porc = '%';

    scanf("%f", &salario);

    if (salario <= 400.00){
        ajuste = 0.15;
        novo = salario * (1 + ajuste);
    }
    else if (400.01 <= salario && salario <= 800.00){
        ajuste = 0.12;
        novo = salario * (1 + ajuste);
    }
    else if (800.01 <= salario && salario <= 1200.00){
        ajuste = 0.10;
        novo = salario * (1 + ajuste);
    }
    else if (1200.01 <= salario && salario <= 2000.00){
        ajuste = 0.07;
        novo = salario * (1 + ajuste);
    }
    else if (salario >= 2000.00){
        ajuste = 0.04;
        novo = salario * (1 + ajuste);
    }

    reajuste = ajuste*salario;

    ajuste = ajuste*100;
    ajuste = (int) ajuste;

    printf("Novo salario: %.2f\n" "Reajuste ganho: %.2f\n" "Em percentual: %.0f %c\n", novo, reajuste, ajuste, porc);

    return 0;
}