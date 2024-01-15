#include <stdio.h>

int main(){

    int N, primeiro = 1, segundo, total = 1;

    scanf("%d", &N);

    for(int i=0; i < N; i ++){

        scanf("%d", &segundo);

        if (primeiro != segundo){
        total ++;
        } 

        primeiro = segundo;
    }
    
    printf("%d\n", total);

    return 0;
}