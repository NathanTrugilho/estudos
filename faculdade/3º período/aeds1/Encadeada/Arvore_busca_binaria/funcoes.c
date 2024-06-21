#include "funcoes.h"

void adiciona(int num, struct no *raiz){
    struct no *aux = raiz;
    while(aux != NULL){
        if(num < aux->value){
            if(aux->esq == NULL){
                aux->esq = (struct no*)malloc(sizeof(struct no));
                aux->esq->value = num;
                aux->esq->dir = NULL;
                aux->esq->esq = NULL;
                return;
            }
            aux = aux->esq;
        }
        if(num > aux->value){
            if(aux->dir == NULL){
                aux->dir = (struct no*)malloc(sizeof(struct no));
                aux->dir->value = num;
                aux->dir->dir = NULL;
                aux->dir->esq = NULL;
                return;
            }
            aux = aux->dir;
        }
        if(aux->value == num){
            printf("O numero ja pertence a arvore!\n ");
            return;
        }
    }
}