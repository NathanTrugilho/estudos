function aprox = Q3d(int,V)
  aprox = eye(length(V));
  for i = 1:int
    aprox = Q3a(aprox,Q3b(Q3c(V^(i-1),V),1/factorial(i)));
  endfor
endfunction