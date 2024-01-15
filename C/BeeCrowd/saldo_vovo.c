#include <stdio.h>

int main (){
    
    int N, S, menor, mov = 0;

    scanf("%d" "%d", &N, &S);

    menor = S;
    
    for (int i = 1; i <= N; i ++){

        scanf("%d", &mov);

        S += mov;
    
        if (S < menor){
            menor = S;
        }

    }
    
    printf("%d\n", menor);
    
    return 0;
}   