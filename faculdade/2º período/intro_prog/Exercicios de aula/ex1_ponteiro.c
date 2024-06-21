#include <stdio.h>

int main(){

    int a = 28, *p1;
    float b = 12, *p2;
    char c = '4', *p3;

    p1 = &a;
    p2 = &b;
    p3 = &c;

    printf("%d\t%p\n%.1f\t%p\n%c\t%p\n", a, p1, b, p2, c, p3);

    return 0;
}