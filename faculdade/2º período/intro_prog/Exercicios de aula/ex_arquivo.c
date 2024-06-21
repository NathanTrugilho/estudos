#include <stdio.h>

typedef struct dados_pessoa
{
    char nome[30], sexo, cor_olhos;
    float altura, peso;

} dados;


int main()
{
    FILE *pt_arquivo, *pt_fem, *pt_men;
    int i = 0;

    pt_arquivo = fopen("dados.txt","r");
    pt_fem = fopen("dadosF.txt", "a");
    pt_men = fopen("dadosM.txt", "a");

    dados person[6];

    //compara para ver se a quantidade de campos ainda e a mesma
    while(fscanf(pt_arquivo, "%s %c %c %f %f", person[i].nome, &person[i].sexo, &person[i].cor_olhos, &person[i].altura, &person[i].peso) == 5)
    {
        i++;
    }

    for(i = 0; i < 6; i++){

        if(person[i].sexo == 'M'){

            fprintf(pt_men,"%s %c %c %f %f\n", person[i].nome, person[i].sexo, person[i].cor_olhos, person[i].altura, person[i].peso);
        }

        if(person[i].sexo == 'F'){

            fprintf(pt_fem,"%s %c %c %f %f\n", person[i].nome, person[i].sexo, person[i].cor_olhos, person[i].altura, person[i].peso);
        }

    }

    fclose(pt_arquivo); fclose(pt_fem); fclose(pt_men);

    return 0;
}