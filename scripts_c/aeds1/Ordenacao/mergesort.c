#include <stdio.h>

void merge(int *vetor, int *vetor_resultado, int e1, int d1, int e2, int d2)
{

    int i = e1, j = e2, k = 0;

    while (i <= d1 && j <= d2)
    {
        if (vetor[i] <= vetor[j])
        {
            vetor_resultado[k] = vetor[i];
            i++;
            k++;
        }
        else
        {
            vetor_resultado[k] = vetor[j];
            j++;
            k++;
        }
    }
    while (i <= d1)
    {
        vetor_resultado[k] = vetor[i];
        i++;
        k++;
    }
    while (j <= d2)
    {
        vetor_resultado[k] = vetor[j];
        j++;
        k++;
    }
    i = e1;
    k = 0;
    while (i <= d2)
    {
        vetor[i] = vetor_resultado[k];
        i++;
        k++;
    }
}

void sort(int *vetor, int *vetor_resultado, int esquerda, int direita)
{

    if (direita > esquerda)
    {
        int meio = (esquerda + direita) / 2;
        sort(vetor, vetor_resultado, esquerda, meio);
        sort(vetor, vetor_resultado, meio + 1, direita);
        merge(vetor, vetor_resultado, esquerda, meio, meio + 1, direita);
    }
}

void main()
{

    int vetor[10] = {1, 78, 2, 6, 0, 4, 6, 8, 4, 23}, vetor_resultado[10];

    sort(vetor, vetor_resultado, 0, 9);
    for (int i = 0; i <= 9; i++)
    {
        printf("%d ", vetor_resultado[i]);
    }
}