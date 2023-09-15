#include <stdio.h>

int main(){

    int segundos, minutos = 0, horas = 0;

    scanf("%d", &segundos);

    while (segundos >= 60){

        minutos ++;
        segundos = segundos - 60;
    }
    while (minutos >= 60){
        
        horas ++;
        minutos = minutos - 60;
    }
    
    printf("%d:" "%d:" "%d\n", horas, minutos, segundos);

    return 0;
}