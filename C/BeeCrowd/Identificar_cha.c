 #include <stdio.h>

 int main (){
    
   int T, A, B, C, D, E, acertos = 0;

   scanf("%d", &T);
   scanf("%d" "%d" "%d" "%d" "%d", &A, &B, &C, &D, &E);

   if(A == T){
      acertos ++;
   }
   if(B == T){
      acertos ++;
   }
   if(C == T){
      acertos ++;
   }
   if(D == T){
      acertos ++;
   }
   if(E == T){
      acertos ++;
   }

   printf("%d\n", acertos);

   return 0;
 }