#include <stdio.h>
#include <stdlib.h>

struct no{
    int value;
    struct no *esq;
    struct no *dir;
};

/*
\brief A função 'adiciona' insere o valor recebido por parâmetro corretamente na Árvore de Busca Binária. 
\param num Numero a ser adicionado.
\param raiz Endereço do nó raiz da árvore.
*/
void adiciona(int num, struct no *raiz);