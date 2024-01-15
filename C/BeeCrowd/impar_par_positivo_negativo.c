#include <stdio.h>

int main(){

    int imp = 0, par = 0, pos = 0, neg = 0, N;

    for (int i = 1; i <= 5; i ++){
        
        scanf("%d", &N);

        if(N%2 != 0){
            imp ++;
        }
        if(N%2 == 0){
            par ++;
        }
        if(N > 0){
            pos ++;
        }
        if(N < 0){
            neg ++;
        }
    }

    printf("%d valor(es) par(es)\n" "%d valor(es) impar(es)\n" "%d valor(es) positivo(s)\n" "%d valor(es) negativo(s)\n", par, imp, pos, neg);

    return 0;
}