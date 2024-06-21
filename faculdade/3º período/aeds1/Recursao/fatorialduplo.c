#include <stdio.h>

int fatd(int n){
    
    if(n == 1 || n == 0) return 1;
    if(n%2 == 0) return fatd(n-1);

    return n * fatd(n-2);
}

int main(){

    printf("%d", fatd(5));

    return 0;
}