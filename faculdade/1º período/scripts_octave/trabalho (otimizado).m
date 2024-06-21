clearvars; clc; tic

%variaveis auxiliares para o codigo

inf = 0;
n = 0;
para = 0;
somadivi = 0;
aux = 1;
multiplo = 0;
qtd = 0; 

%definindo uma repeticao infinita
while inf == 0
  n += 1;
  
  %verifica a soma dos divisores
  if((mod(n,2) == 0))
    for dividir = (1:n/2), 
      if (mod (n, dividir) == 0)
        somadivi += dividir;
      endif
    endfor
  endif
  
  %verifica se a soma dos divisores e igual ao numero (ver se e perfeito)
  if (somadivi == n)
    %mostra o numero perfeito
    disp(somadivi)
    % guarda a quantidade de numeros perfeitos
    para += 1;
  endif
  
  %reseta a variavel para refazer o loop
  somadivi = 0;
  
  %interrompe a repeticao quando são identificados quatro numeros perfeitos
  if (para == 4)
    break
  endif
endwhile

%toc (usado durante a otimização do código)

%cria uma repeticao ate n (ultimo numero perfeito)
while aux < n
  aux += 1;
  
  % guarda a quantidade de multiplos do numero dentro da repeticao
   for i = 1:sqrt(aux), 
     if (mod (aux, i) ==0)
       multiplo += 1;
     endif
   endfor
   
  %verifica se o numero e primo ( se tem apenas um multiplo (dado pelas circunstancias do nosso codigo que nao considera a divisao do numero por ele mesmo), e primo)
  if (multiplo == 1)
    %armazena a quantidade de numeros primos encontrados
    qtd += 1  ;
  endif
  %reseta a variavel para uma nova repeticao
  multiplo = 0;
endwhile

%mostra a quantidade de numeros primos
disp('a quantidade de numeros primos menores que o ultimo perfeito é:'), disp(qtd)

toc %tempo total