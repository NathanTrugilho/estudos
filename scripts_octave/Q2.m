function [soma] = Q2(v1,i,j)
  
  soma = 0;
  divisores = 0 ;
  tamanho = size(v1);
  
  if (i + 1 <= tamanho(1) ) 
    soma = soma + v1(i + 1 , j);
    divisores = divisores + 1;
  endif
  
  if (i - 1 > 0)    
    soma = soma + v1(i - 1 , j);
    divisores = divisores + 1;
  endif
  
  if (j + 1 <= tamanho(2) )
    soma = soma + v1( i , j + 1);
    divisores = divisores + 1;
  endif
  
  if (j - 1 > 0)
    soma = soma + v1(i  , j - 1);
    divisores = divisores + 1;
  endif
  
  soma = soma / divisores ;
endfunction