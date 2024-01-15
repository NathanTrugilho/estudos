#include <stdio.h>

int main(){
    
    char nome;
    double salario, vendas;

    scanf("%s\n", &nome); 
    scanf("%lf\n", &salario);
    scanf("%lf", &vendas);

    printf("TOTAL = R$ %.2lf\n", salario + 0.15*vendas);
    
    return 0;
}