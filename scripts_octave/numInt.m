function area = numInt(f1, f2, a, b, N, Metodo, Display)

area = 0;

if Metodo == 0

   dist = (b-a)/N;
   quadrado = a:dist:b-dist;

   for i=1:N
      if f1(quadrado(i)) > f2(quadrado(i))
         if Display == 0
            hold on; grid on;
            vertices = [quadrado(i) f1(quadrado(i));
                        quadrado(i)+dist f1(quadrado(i));
                        quadrado(i)+dist f2(quadrado(i));
                        quadrado(i) f2(quadrado(i))];
            fill(vertices(:,1), vertices(:,2), 'b');
         endif
         area = area + (f1(quadrado(i))-f2(quadrado(i)))*dist;
      else
         if Display == 0
            hold on; grid on;
            vertices = [quadrado(i) f2(quadrado(i));
                        quadrado(i)+dist f2(quadrado(i));
                        quadrado(i)+dist f1(quadrado(i));
                        quadrado(i) f1(quadrado(i))];
            fill(vertices(:,1), vertices(:,2), 'b');
         endif
         area = area + (f2(quadrado(i))-f1(quadrado(i)))*dist;
      endif
   endfor

else

   dist = (b-a)/N;
   quadrado = a:dist:b-dist;

   for i=1:N
      if f1(quadrado(i)) > f2(quadrado(i))
         if Display == 0
            hold on; grid on;
            vertices = [quadrado(i) f1(quadrado(i));
                        quadrado(i) f2(quadrado(i));
                        quadrado(i)+dist f2(quadrado(i)+dist);
                        quadrado(i)+dist f1(quadrado(i)+dist)];
            fill(vertices(:,1), vertices(:,2), 'b');
         endif
         Base1 = f1(quadrado(i))-f2(quadrado(i));
         Base2 = f1(quadrado(i)+dist)-f2(quadrado(i)+dist);
         area = area + (Base1+Base2)*dist/2;
      else
         if Display == 0
            hold on; grid on;
            vertices = [quadrado(i) f2(quadrado(i));
                        quadrado(i) f1(quadrado(i));
                        quadrado(i)+dist f1(quadrado(i)+dist);
                        quadrado(i)+dist f2(quadrado(i)+dist)];
            fill(vertices(:,1), vertices(:,2), 'b');
         endif
         Base1 = f2(quadrado(i))-f1(quadrado(i));
         Base2 = f2(quadrado(i)+dist)-f1(quadrado(i)+dist);
         area = area + (Base1+Base2)*dist/2;
      endif
   endfor
endif

   if Display == 0
      hold on; grid on;
      linha = a:0.01:b;

      xlim([a b]);
      plot(linha, f1(linha), 'LineWidth', 2, 'Color', 'k');
      plot(linha, f2(linha), 'LineWidth', 2, 'Color', 'k');
      pbaspect([1 1 1]);
   endif

endfunction
