#include <stdio.h>

struct balao{
    short altura;
    short estourado;
};

short main(){
    short quantidade_de_baloes, flechas_necessarias = 0;

    //Recebe a quantidade de balões e cria um vetor com tamanho suficiente pra armazenar todas as posições
    scanf("%d", &quantidade_de_baloes);
    struct balao posicao_dos_baloes[quantidade_de_baloes];

    //Recebe e guarda a posição dos balões no vetor
    for(short i = 0; i < quantidade_de_baloes; i++){
        scanf("%d", &posicao_dos_baloes[i].altura);
        
        //Estou definindo os balões como não estourados. Isso serve para identificar um balão como estourado ou não (vai ser usado no futuro)
        posicao_dos_baloes[i].estourado = 0; 
    };

    //Percorre o vetor de posições estourando os baloes e fazendo as contas
    for(short i = 0; i < quantidade_de_baloes; i++){
        for(short j = i; j < quantidade_de_baloes; j++){

            if(posicao_dos_baloes[i].altura == posicao_dos_baloes[j].altura + 1){
                posicao_dos_baloes[j].estourado = 1;
                break;
            }
        }
        if(posicao_dos_baloes[i].estourado == 0) flechas_necessarias++;
    }
    printf("%d", flechas_necessarias);
    return 0;
}