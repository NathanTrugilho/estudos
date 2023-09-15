function  k = Q3e(limit,L)
  
  hold on ;
  
  grid on;
  
  pbaspect([1 1 1]) ;
  
  for i = 1:limit
    
    plot(i,det(Q3d(i,L)),'p');
    
  endfor
endfunction