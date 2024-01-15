#include <stdio.h>

int main (){
    int multiplicador = 1, xp = 1, resultado, flag = 1;

    while (flag = 1){
        scanf("%d" "%d", &multiplicador, &xp);

        resultado = xp * multiplicador;

        if(multiplicador == 0 && xp == 0){
            break;
        }

        printf("%d\n", resultado);

    }
    return 0;
}

