function nada = myFunc2(vet)

  %calcula o tamanho do vetor que sera usado nos calculos;
  tamanho = length(vet);

  %calcula a media aritmetica;
  media_aritmetica = sum(vet)/tamanho;

  %calcula a media geometrica;
  media_geometrica = (prod(vet))^(1/tamanho);

  %printa os resultados encontrados
  disp("\nA media aritmetica do vetor e:");
  disp(media_aritmetica);
  disp("\nA media geometrica do vetor e:");
  disp(media_geometrica);

endfunction;
