function c = Q1(v1,v2)
  c = [];
  v1 = v1(2:length(v1 - 1));
  v2 = v2(2:length(v2 - 1));
  v1 = unique(v1);
  v2 = unique(v2);
  for i = 1:length(v1),
    for k = 1:length(v2),
      if (v1(i) == v2(k))
        c(i) = v1(i);
      endif
    endfor  
  endfor
 guarda = 0;
 guarda = c(1);
 c(1) = length(c);
 c(length(c) + 1) = guarda ;
endfunction