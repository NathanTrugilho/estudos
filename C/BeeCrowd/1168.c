#include <stdio.h>
#include <string.h>

int main(){

    int N, tam, total;
    char led[105], num;

    scanf("%d", &N);

    for(int i = 0; i < N; i++){
        
        total = 0;
        scanf("%s", led);
        tam = strlen(led);

        for(int j = 0; j < tam; j++){

            num = led[j];

            if (num == '1') total += 2;
            
            if (num == '2' || num == '3' || num == '5') total += 5;

            if (num == '4') total += 4;

            if (num == '6' || num == '9' || num == '0') total += 6;

            if (num == '7') total += 3;

            if (num == '8') total += 7;

        }
        printf("%d leds\n", total);
    }
    return 0;
}