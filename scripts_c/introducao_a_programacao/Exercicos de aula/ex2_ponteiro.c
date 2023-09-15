#include <stdio.h>

int main(){

    char vetc[5] = "2004", *pc;
    int veti[5], *pi, bag; 
    float vetf[5], *pf; 
    
    veti[0] = 2;
    veti[1] = 0; 
    veti[2] = 0; 
    veti[3] = 4;

    vetf[0] = 2.0;
    vetf[1] = 0.0; 
    vetf[2] = 0.0; 
    vetf[3] = 4.0;  
    
    printf("\n");

    for(int i = 0; i < 5; i++){

        pc = &vetc[i];
        printf("%p\t", pc);
    }
    printf("\n");

    for(int i = 0; i < 5; i++){

        pi = &veti[i];
        bag = veti[i];

        printf("%p\t", pi);
    }
    printf("\n");

    for(int i = 0; i < 5; i++){

        pf = &vetf[i];
        printf("%p\t", pf);
    }
    printf("\n\n");

    return 0;
}