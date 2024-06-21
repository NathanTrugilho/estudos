% Programado na versão 7.2.0;

% Feito por Nathan Trugilho Braga

% Importante rodar o código antes de chamar a função (para definir o x como symbol e dar load na biblioteca)

% Só é necessario rodar UMA vez. Após rodar pela primeira vez, não usar o 'clearvars' na janela de comandos, pois x terá que ser definido novamente como symbol.

%carrega a biblioteca
pkg load symbolic;

%limpa o ambiente
clearvars;
clc;

%legenda para auxiliar o usuário
disp("\n************** Entre com os dados da função: **************\n                                                          *")
disp(" Não funciona com equações de duas ou mais sentenças!!!   *\n                                                          *")
disp(" Formatação: grafico((função), modo, x0)                  *\n                                                          *")
disp(" Modo: '1' para mostrar propriedades de derivada          *")
disp("  '0' para exibir apenas o grafico (nao necessita de x0!) *\n                                                          *")
disp(" Exemplo de utilização: grafico((x.^3 + x + 3), 1, 0)     *")
disp(" Exemplo de utilização: grafico(((x+4)./(x+2)), 1, 0)     *")
disp(" Exemplo de utilização: grafico((x.^2 - 2), 0)            *\n                                                          *")
disp(" (Utilize '.^' para potenciação e './' para divisão!)     *\n                                                          *")
disp("         Sugestão de modelo para assintota:               *")
disp("        plot([x x],[y y],'--b','linewidth',2.5)           *\n                                                          *")
disp("***********************************************************\n")

%define X como symbol para exibir as equações na janela de comandos
syms x;

  function nathan = grafico(f, modo, inicial)

  %será usado mais pra frente!
  v = true;
  close all;

    if modo == 1 || modo == 0

        hold on;

        %usado para exibir o grafico com as propriedades da derivada
        if modo == 1

            %calcula a equação da derivada em 'f' e guarda em 'coef' como symbol
            coef = diff(f);

            disp("\n************************************************")
            disp("\n A equacao da derivada e:\n")
            %salva em outra variavel para ser usado novamente
            eq = coef;

            %exibe a equacao da derivada de 'f' em symbol
            disp(eq);

            %transforma 'coef' (symbol) em function_handle para ser usado mais à frente
            coef = function_handle(coef);

            %auxiliar para funções lineares
            lin = func2str(coef);

            %utilizado para debugar em funções lineares. (O handle do 'coef' fica como @(), impossibilitando o uso em 'm' (linha 72) e gerando um 'error'

            %Com isso, o @() vira @(x), tornando possível 'm = coef(inicial)'
            if lin(3) != 'x'

              lin(3) = 'x';
              lin(4) = ')';

              coef = str2func(lin);

            endif

            %transforma 'f' (antes symbol que foi utilizado para definir a eq da derivada (linha 38)) em function_handle para ser usado
            f = function_handle(f);

            %calcula o coef. angular no ponto x0(inicial)
            m = coef(inicial);

            %calcula o y0 no ponto x0(inicial)
            y0 = f(inicial);

            %define 'inicial' como 'x0' para ser usado no calculo da eq da reta (symbol) no ponto x0(inicial)
            x0 = inicial;

            %coef. angular que vai ser usado para exibir a equacao da reta

            c = num2str(m);

            %exibe o coef. angular na janela de comandos
            disp("\n O coeficiente angular no ponto é igual a:\n"), disp(c);

            %necessario para exibir a eq. da reta
            syms x;

            %exibe a eq. da reta na janela de comandos
            %(talvez dê merda caso seja algum float!!!)
            disp("\n A equacao da reta e dada por y = \n")
            disp(y0 + c .*(x - x0)), disp("")

            %desativa o 'warning' para quando o valor acima for em float!
            [~, id] = lastwarn ();
            warnstate = warning ("off");

            %Transforma o X para valores numéricos a fim de fazer o calculo da eq. da reta que será plotada
            x = -45:0.1:45;

            %eq. da reta que será plotada
            y = @(x)(f(inicial) +  coef(inicial) * (x - inicial));

            %eq. da reta normal (achei que não seria muito útil plotar, mas deixei salvo aqui caso precise).
            %yn = @(x)(f(inicial) +  (-(x - inicial)/coef(inicial)));

            %plota os eixos X, Y
            plot([-45 45 ],[0 0], 'k','linewidth',1.25);
            plot([0 0],[-30 30], 'k','linewidth',1.25);

            %plota a função 'f', a eq. da reta 'y' e o ponto de tangência 'y(x0)'
            p1 = plot(x,f(x),'r','linewidth',2.5, x,y(x), 'g', 'linewidth',2.5, inicial,y(inicial),'ob', 'markersize', 7, 'markerfacecolor','b');

            %cria e ajusta a legenda
            legend(p1,'Função inicial', 'Função linear em x0','Ponto de tangência em x0');
            legend (p1, 'location','northeastoutside');

        %usado para exibir apenas o grafico
        else

            %mesma coisa do outro
            f = function_handle(f);

            x = -45:0.1:45;

            plot([-45 45 ],[0 0], 'k','linewidth',1.25);
            plot([0 0],[-30 30], 'k','linewidth',1.25);

            p2 = plot(x,f(x),'r','linewidth',2.5);
            %legend(p2,'Função inicial');
            %legend ('location','northeastoutside');

        endif

    else
        %exibe uma mensagem de erro caso o 'modo' seja diferente de 1 ou 0

        disp("\n ***Erro!***\n")
        v = false;

    endif

    %usado para nao exibir o grafico em branco caso haja algum erro na entrada

    if v == true

      %ajusta o tamanho da exibição do eixo
      axis ([-15 15  -10 10])

      %ajusta o titulo
      title ('Gráfico da função')
      set(gca,'fontsize',22)

      %formatação do grafico
      box on;
      grid minor on;

      %exibe os rotulos de X e Y
      ylabel('f(x)')
      xlabel('x')
      %trava a proporção de exibição
      pbaspect([3/2 1]);

    endif

endfunction;
