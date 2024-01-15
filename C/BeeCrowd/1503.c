#include <stdio.h>
#include <string.h>

int main(){
    
    char mensagem[50001], chat[10][50001], verificar[50001];
    int qtd_msg, tamanho_str, tamanho_menor_str = 50001, indice_menor;

    //encontra a quantidade de mensagens que serao recebidas
    scanf("%d", &qtd_msg);

    //guarda as mensagens na matriz "chat", descobrindo em qual indice está a menor mensagem que sera verificada
    for(int i = 0; i < qtd_msg; i++){

        scanf("%s", mensagem);

        tamanho_str = strlen(mensagem);
        
        if(tamanho_str <= tamanho_menor_str){

            tamanho_menor_str = tamanho_str;

            indice_menor = i;
        }

        for(int j = 0; j < tamanho_str; j++){

            chat[i][j] = mensagem[j];
        }   
    }
    
    //verifica os palindromos impares:
    for(int i = 0, termos = 1, volta = 0, comp_palind = 0; i < strlen(chat[indice_menor]); i++){
        
        //condicao de entrada do palindromo impar (ex: aba, ala, ana)
        if(chat[indice_menor][i - 1] == chat[indice_menor][i + 1]){

            //loop para imprimir o palindromo
            for(int j = 1; j < tamanho_menor_str; j++){
                
                //verifica se ainda e um palindromo a fim de retornar o loop (ex: ababa)
                if(chat[indice_menor][i - j] == chat[indice_menor][i + j]){   
                    
                    //usados para guardar o palindromo no vetor
                    termos += 2;
                    volta ++;
                    
                    //evita um loop infinito (ex de caso: ala)
                    if((i - j) < 0) break;

                    printf(" ");

                    //guarda o palindromo num vetor
                    for(int k = 0; k < termos; k++){

                        verificar[k] = chat[indice_menor][(i - volta) + k];   
                    }
                    
                    //imprime o mesmo
                    for(int j = 0; j < termos; j++){

                        printf("%c", verificar[j]);
                    }
                }

                //corta o loop caso nao seja mais um palindromo
                else{

                    termos = 1;
                    volta = 0;
                    break;
                }
            } 
            printf(" ");
        }
    }

    //verifica os palindromos pares:
    for(int i = 0, termos = 0, volta = 0, comp_palind = 0; i < strlen(chat[indice_menor]); i++){
        
        //condicao de entrada do palindromo par (ex: aa, bbbb, abba)
        if(chat[indice_menor][i] == chat[indice_menor][i + 1]){
            
            //loop para caso o palindromo seja maior que o caso base (caso base ex: bb), (maior que o caso base ex: babbab)
            for(int j = 0; j < tamanho_menor_str; j++){
                
                //verifica se ainda e um palindromo
                if(chat[indice_menor][i - j] == chat[indice_menor][i + (j+1)]){   
                    
                    //usados para guardar o palindromo no vetor
                    termos += 2;
                    
                    //evita um loop infinito (ex de caso: bb)
                    if((i - j) < 0) break;

                    printf(" ");
                    
                    //guarda o palindromo no vetor
                    for(int k = 0; k < termos; k++){

                        verificar[k] = chat[indice_menor][(i - volta) + k];   
                    }
                    
                    volta ++;

                    //imprime o palindromo
                    for(int j = 0; j < termos; j++){

                        printf("%c", verificar[j]);
                    }
                }
                
                //corta o loop caso nao seja mais um palindromo
                else{

                    termos = 0;
                    volta = 0;
                    break;
                }
            } 
            printf(" ");
        }
    }

    return 0;
}