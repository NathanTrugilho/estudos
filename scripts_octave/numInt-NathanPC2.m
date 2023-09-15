function somatorio = numInt (f1, f2, a, b, N, Metodo, Display)

%valor da area a retornar
somatorio = 0;

%executa o metodo de aproximacao da area quadrada
if Metodo == 0

   %define a largura de cada retangulo
   largura = (b-a)/N;
   x = a:largura:b-largura;

   %inicia o somatorio das areas dos retangulos
   for i=1:N
      %checa qual das duas funcoes retorna maior valor no momento i
      if f1(x(i)) > f2(x(i))
         %checa se e necessario plotar o grafico
         if Display == 0
            hold on; grid on;
            %plota todos o retangulo observado em i no grafico utilizando a funcao rectangle
            rectangle('Position', [x(i) f2(x(i)) largura (f1(x(i))-f2(x(i)))], 'FaceColor', 'b', 'EdgeColor', 'k');
         endif
         %soma a area do retangulo observado em i no somatorio total
         somatorio = somatorio + ((f1(x(i))-f2(x(i)))*largura);
      else
         if Display == 0
            hold on; grid on;
            rectangle('Position', [x(i) f1(x(i)) largura (f2(x(i))-f1(x(i)))], 'FaceColor', 'b', 'EdgeColor', 'k');
         endif
         somatorio = somatorio + ((f2(x(i))-f1(x(i)))*largura);
      endif
   endfor

%executa o metodo de aproximacao da area trapezoidal
else

   largura = (b-a)/N;
   x = a:largura:b-largura;

      %inicia o somatorio das areas dos trapezios
      for i=1:N
         if f1(x(i)) > f2(x(i))
            if Display == 0
               hold on; grid on;
               %encontra os 4 vertices do trapezio observado em i
               vertices = [x(i) f2(x(i));
                           x(i)+largura f2(x(i)+largura);
                           x(i)+largura f1(x(i)+largura);
                           x(i) f1(x(i))];
               %plota o trapezio observado em i utilizando a funcao fill
               fill(vertices(:, 1), vertices(:, 2), 'b');
            endif
            %calcula as duas bases do trapezio observado em i e as utiliza para calcular a area
            Base1 = f1(x(i))-f2(x(i));
            Base2 = f1(x(i)+largura)-f2(x(i)+largura);
            Area = (Base1+Base2)*largura/2;

            %soma a area encontrada no somatorio total
            somatorio = somatorio + Area;
         else
            if Display == 0
               hold on; grid on;
               vertices = [x(i) f1(x(i));
                           x(i)+largura f1(x(i)+largura);
                           x(i)+largura f2(x(i)+largura);
                           x(i) f2(x(i))];
               fill(vertices(:, 1), vertices(:, 2), 'b');
            endif
            Base1 = f2(x(i))-f1(x(i));
            Base2 = f2(x(i)+largura)-f1(x(i)+largura);
            Area = (Base1+Base2)*largura/2;
            somatorio = somatorio + Area;
         endif
      endfor

endif

   %checa se e necessario plotar o grafico
   if Display == 0
      %define o titulo com o resultado encontrado
      title(horzcat("Area aproximada: ", num2str(somatorio)));

      %plota as duas curvas
      frequencia =  a:0.01:b;
      plot(frequencia, f1(frequencia), 'LineWidth', 2, 'Color', 'k');
      plot(frequencia, f2(frequencia), 'LineWidth', 2, 'Color', 'k');

      %formata o grafico
      xlim([a b]);
      set(gca, 'FontSize', 18);
      pbaspect([1 1 1]);
   endif

endfunction

%Ana Luiza Lima Vila Real Rosa
%Arthur Illa Bonilha de Souza
%Breno Nery de Freitas
%Caio Cesar Camillo Machado Ramos
%Carlos Augusto Teles Gomes Junior
%Daniel Matos Coelho
%Emanuel da Silva Cabral
%Gabriel Lopes de La Puente
