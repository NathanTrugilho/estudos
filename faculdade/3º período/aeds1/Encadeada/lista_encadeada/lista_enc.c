#include <stdio.h>
#include <stdlib.h>

struct no{
    char letra;
    struct no *ponteiro_prox;
};

void aloca(char c, struct no *prox){  
    // o ponteiro "aux" recebe o endereco de onde o novo no foi alocado
    struct no *aux = malloc(sizeof(struct no));
    //o novo no recebe o conteudo e o ponteiro para NULL por ser o ultimo no da lista encadeada
    aux->letra = c;
    aux->ponteiro_prox = NULL;

    //Processo para encontrar o ultimo elemento da lista encadeada
    //verificacao: se o campo ponteiro_prox (ponteiro para uma estrutura no) da estrutura "prox" estiver apontando para NULL, logo este sera o ultimo no da lista
    //a variavel "prox" nao representa uma estrutura em si, mas sim um endereco de uma estrutura. 
    //Entao, quando faco "prox->ponteiro_prox", acesso o campo "ponteiro_prox" da estrutura que esta guardada no endereco "prox"
    while (prox->ponteiro_prox != NULL){
        //prox vai receber o endereco da proxima estrutura, dando continuidade à lista
        prox = prox->ponteiro_prox;
    }
    //faco o ultimo elemento da lista apontar para a estrutura aux, fazendo, assim, um link entre as estruturas
    prox->ponteiro_prox = aux;
}

void desaloca(char c, struct no *prox){
    struct no *p;
    //Faz a varredura ate encontrar o elemento a ser apagado ou ate acabar a lista encadeada
    while (prox -> ponteiro_prox -> ponteiro_prox != NULL && prox -> ponteiro_prox -> letra != c){
        prox = prox -> ponteiro_prox;
    } 
    //Verificacao para caso o elemento a ser desalocado seja o ultimo 
    if(prox -> ponteiro_prox -> letra == c && prox -> ponteiro_prox -> ponteiro_prox == NULL){
        p = prox -> ponteiro_prox;
        prox -> ponteiro_prox = NULL;
        free(p);
        return;
    }
    //Feedback caso o elemento nao esteja na lista encadeada
    if(prox -> ponteiro_prox -> ponteiro_prox == NULL){
        printf("Elemento nao encontrado \n");
        return;
    }
    //faz a desalocacao do elemento
    p = prox -> ponteiro_prox;
    prox -> ponteiro_prox = prox -> ponteiro_prox ->ponteiro_prox;
    free(p);
}

void limpa_mem(struct no *prox){
    struct no *aux;
    //Condicao de parada para a varredura
    while(prox -> ponteiro_prox != NULL){
        //salva o endereco "anterior" num ponteiro auxiliar para usar o "free()"
        aux = prox;
        //avanca um termo na lista encadeada
        prox = prox -> ponteiro_prox;
        free(aux);
    }
    free(prox);
}

// Função para imprimir a lista
void printa_enc(struct no *prox) {
    while (prox != NULL) {
        printf("%c ", prox ->  letra);
        prox = prox -> ponteiro_prox;
    }
}

int main(){

    //Crio um ponteiro que aponta para o no cabeca
    struct no *cab = malloc(sizeof(struct no));
    
    //Faco com que o no cabeca aponte para null por so ter um elemento
    cab -> ponteiro_prox = NULL;

    aloca('N', cab);
    aloca('A', cab);
    aloca('T', cab);
    aloca('H', cab);
    aloca('A', cab);
    aloca('N', cab);

    printa_enc(cab -> ponteiro_prox);
    printf("\n");

    desaloca('H', cab);

    printa_enc(cab -> ponteiro_prox);
    limpa_mem(cab);

    return 0;
}