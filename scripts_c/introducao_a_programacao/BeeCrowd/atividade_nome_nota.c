#include <stdio.h>

    int main (){
    
    char nome[10], nome2[10], nome3[10], nome4[10], nome5[10], nome6[10];
    float nota, nota2, nota3, nota4, nota5, nota6;
  
    scanf("%s", &nome);
    scanf("%f", &nota);

    scanf("%s", &nome2);
    scanf("%f", &nota2);
    
    scanf("%s", &nome3);
    scanf("%f", &nota3);

    scanf("%s", &nome4);
    scanf("%f", &nota4);
   
    scanf("%s", &nome5);
    scanf("%f", &nota5);

    scanf("%s", &nome6);
    scanf("%f", &nota6);

    printf("1. %s %.2f\n", nome, nota);
    printf("2. %s %.2f\n", nome2, nota2);
    printf("3. %s %.2f\n", nome3, nota3);
    printf("4. %s %.2f\n", nome4, nota4);
    printf("5. %s %.2f\n", nome5, nota5);
    printf("6. %s %.2f\n", nome6, nota6);

    return 0;
}