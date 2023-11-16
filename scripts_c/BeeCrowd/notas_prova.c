#include <stdio.h>

int main (){

    int N;

    scanf("%d", &N);

    if (N == 0){
        printf("E\n");
    }
    else if (1 <= N && N <= 35){
        printf("D\n");
    }
    else if (36 <= N && N <= 60){
        printf("C\n");
    }
    else if (61 <= N && N <= 85){
        printf("B\n");
    }
    else if (N >= 86){
        printf("A\n");
    }

    return 0;
}