#include <stdio.h>
#include <stdlib.h>

#define TAMANHO_VETOR 10

int* make_set(int n)
{
    int* vetor = (int*)malloc(sizeof(n*sizeof(int)));
    for (int i = 0; i < TAMANHO_VETOR; i++)
    {
        *(vetor + i) = i;
    }
    return vetor;
}

int find_set(int* vetor, int vertice)
{
    return vetor[vertice];
}

void union_set(int *vetor, int vertice1, int vertice2)
{
    int rep1 = find_set(vetor, vertice1);
    int rep2 = find_set(vetor, vertice2);

    for(int i = 0; i < TAMANHO_VETOR; i++)
    {
        if (vetor[i] == rep2)
        {
            vetor[i] = rep1;
        }
    }
}

void main()
{
    int* vetor = make_set(TAMANHO_VETOR);

    union_set(vetor, 1,2);
    union_set(vetor, 1,4);
    union_set(vetor, 2,8);
    
    for (int i = 0; i < TAMANHO_VETOR; i++)
    {
        printf("%d ", vetor[i]);
    }
    free(vetor);
}