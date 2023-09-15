#include <stdio.h>

void adicao(int n, int mat1[][n], int  mat2[][n]){

    int matr[n][n];

    for(int l = 0; l < n; l++){
        for(int c = 0; c < n; c++){

            matr[l][c] = mat1[l][c] + mat2[l][c];
        }
    }

    printf("A soma das matrizes e igual a:\n\n");

    for(int l = 0; l < n; l++){
        printf("\t  [");
        for(int c = 0; c < n; c++){

            printf(" %d ", matr[l][c]);
        }
        printf("]\n");
    }
    printf("\n");
}

void diferenca(int n, int mat1[][n], int  mat2[][n]){

    int matr[n][n];

    for(int l = 0; l < n; l++){
        for(int c = 0; c < n; c++){

            matr[l][c] = mat1[l][c] - mat2[l][c];
        }
    }

    printf("A diferenca das matrizes e igual a:\n\n");

    for(int l = 0; l < n; l++){
        printf("\t  [");
        for(int c = 0; c < n; c++){

            printf(" %d ", matr[l][c]);
        }
        printf("]\n");
    }
    printf("\n");
}

void produto(int n, int mat1[][n], int  mat2[][n]){

    int matr[n][n];

    for(int l = 0; l < n; l++){

        for(int c=0 ; c < n; c++){

            int somaprod = 0;

            for(int i=0; i<n; i++){

                somaprod += mat1[l][i]*mat2[i][c];
                matr[l][c] = somaprod;

            }
        }
    }
     printf("O produto das matrizes e igual a:\n\n");

    for(int l = 0; l < n; l++){
        printf("\t  [");
        for(int c = 0; c < n; c++){

            printf(" %d ", matr[l][c]);
        }
        printf("]\n");
    }
    printf("\n");

}


int main(){
    
    int n = printf("Digite a ordem das matrizes: ");
    scanf("%d",&n);
    int mat1[n][n] , mat2[n][n];

    printf("Os valores serao preenchidos linha a linha!\n");
    printf("Introduza valores para a primeira matriz: \n");
    
    for(int l = 0; l < n; l++){
        for(int c = 0; c < n; c++){

            int v; scanf("%d", &v);
            mat1[l][c] = v;
        }
    }
    
    printf("Introduza valores para a segunda matriz: \n");
    for(int l = 0; l < n; l++){
        for(int c = 0; c < n; c++){

            int v; scanf("%d", &v);
            mat2[l][c] = v;
        }
        printf("\n");
    }

    printf("As matrizes digitadas sao:\n\nmatriz 1:\n");
    for(int l = 0; l < n; l++){
        printf("\t  [");
        for(int c = 0; c < n; c++){

            printf(" %d ", mat1[l][c]);
        }
        printf("]\n");
    }
    printf("\n");

    printf("matriz 2:\n");
    for(int l = 0; l < n; l++){
        printf("\t  [");
        for(int c = 0; c < n; c++){

            printf(" %d ", mat2[l][c]);
        }
        printf("]\n");
    }
    printf("\n");

    adicao(n, mat1, mat2);
    diferenca(n, mat1, mat2);
    produto(n, mat1, mat2);

    return 0;
}