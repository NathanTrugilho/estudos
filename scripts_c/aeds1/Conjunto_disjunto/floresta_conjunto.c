#include <stdio.h>

#define TAMANHO_PAI_RANK 6

void make_set(int *pai, int *rank, int conteudo)
{
    pai[conteudo] = conteudo;
    rank[conteudo] = 0;
}

int find_set(int *pai, int conteudo)
{
    while (pai[conteudo] != conteudo)
    {
        conteudo = pai[conteudo];
    }  
    return conteudo;
}

int find_set_path_compression(int *pai, int conteudo)
{
    if(conteudo != pai[conteudo])
    {       
        pai[conteudo] = find_set_path_compression(pai, pai[conteudo]);
    }
    return pai[conteudo];
}

void union_by_rank(int *pai, int *rank, int vertice_1, int vertice_2)
{
    int raiz_v1 = find_set_path_compression(pai, vertice_1);
    int raiz_v2 = find_set_path_compression(pai, vertice_2);

    if(raiz_v1 == raiz_v2) return;

    if(rank[raiz_v1] < rank[raiz_v2])
    {
        pai[raiz_v1] = raiz_v2;
    }

    else
    {
        pai[raiz_v2] = raiz_v1;

        if(rank[raiz_v1] == rank[raiz_v2])
        {
            rank[raiz_v1] += 1;
        }
    }
}

int main()
{
    int pai[TAMANHO_PAI_RANK], rank[TAMANHO_PAI_RANK];

    for(int i=0; i<TAMANHO_PAI_RANK; i++)
    {   
        make_set(pai, rank, i);
    }

    union_by_rank(pai, rank, 0, 1);
    union_by_rank(pai, rank, 0, 2);
    union_by_rank(pai, rank, 4, 3);
    union_by_rank(pai, rank, 5, 3);
    union_by_rank(pai, rank, 1, 4);


    printf("\n Vetor de pais:  [%d, %d, %d, %d, %d, %d]", pai[0], pai[1], pai[2], pai[3], pai[4], pai[5]);
    printf("\n Vetor de ranks: [%d, %d, %d, %d, %d, %d]\n\n", rank[0], rank[1], rank[2], rank[3], rank[4], rank[5]);

    return 0;
}