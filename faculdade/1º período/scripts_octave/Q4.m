function dias = Q4(C,D)
  dias = (C.ano*365 + C.mes*30 + C.dia) - (D.ano*365 + D.mes*30 + D.dia);
  dias = abs(dias);
endfunction