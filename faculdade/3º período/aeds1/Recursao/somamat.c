#include <stdio.h>

void main(){

    int matA[2][2] = {{1,2},{3,4}}, matB[2][2] = {{-1,-2},{-3,-4}};
    int matR[2][2];

    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            matR[i][j] = matA[i][j] + matB[i][j];
        }
    }

    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            printf("%d", matR[i][j]);
        }
    }
}