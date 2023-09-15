//Arvore de busca binaria
#include "funcoes.h"

int main(){
    
    struct no *raiz = (struct no*)malloc(sizeof(struct no));
    raiz->value = 150;
    raiz->esq = NULL; 
    raiz->dir = NULL;

    adiciona(90, raiz);

    return EXIT_SUCCESS;
}
