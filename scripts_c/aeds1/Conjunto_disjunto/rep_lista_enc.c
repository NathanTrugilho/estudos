#include <stdio.h>
#include <stdlib.h>

#define QUANTIDADE_NOS 10

struct no{
    int elemento;
    struct no* prox;
    struct no* rep;
};

struct vetno{
    int qtd;
    struct no* cab;
};

void make_set(struct vetno *vet)
{
    for(int i = 0; i < QUANTIDADE_NOS; i++)
    {
        (vet + i) -> qtd = 0;
        (vet + i) -> cab = (struct no*)malloc(sizeof(struct no));
        (vet + i) -> cab -> elemento = i;
        (vet + i) -> cab -> rep = (vet + i) -> cab;
        (vet + i) -> cab -> prox = NULL;
    }
}

struct no* find_set(struct vetno *vet, int elemento)
{
    return (vet + elemento) -> cab -> rep; 
}

void set_union(struct vetno *vet, int elemento1, int elemento2)
{
    struct no* rep1 = find_set(vet, elemento1);
    struct no* rep2 = find_set(vet, elemento2);
    struct no* aux;

    if((vet + elemento1) -> qtd > (vet + elemento2) -> qtd)
    {
        (vet + elemento1) -> qtd ++; 
        aux = (vet + elemento1) -> cab;
        while (aux -> prox != NULL)
        {
            aux = aux -> prox;
        }
        aux -> prox = (vet + elemento2) -> cab;

        aux = (vet + elemento2) -> cab;
        while (aux != NULL)
        {
            aux -> rep = rep1;
            aux = aux -> prox;
        }
    }

    else
    {
        (vet + elemento2) -> qtd ++; 
        aux = (vet + elemento2) -> cab;
        while (aux -> prox != NULL)
        {
            aux = aux -> prox;
        }
        aux -> prox = (vet + elemento1) -> cab;

        aux = (vet + elemento1) -> cab;
        while (aux != NULL)
        {
            aux -> rep = rep2;
            aux = aux -> prox;
        }
    }
}

int main()
{
    struct vetno vet[QUANTIDADE_NOS];
    make_set(vet);

    set_union(vet,1,2);

    if((vet + 2) -> qtd == 1) printf("AAAAAAAAAAAAAAAAAAAAAAAAAAAA");

    return 0;
}