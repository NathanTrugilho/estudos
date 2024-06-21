% =====================================================
% CEFET-RJ Campus Petropolis
% Faculdade de Engenharia de Computação
% GCOM1001PE - Introdução à Engenharia - 2022/1
% Prof. Rafael Saraiva Campos
% =====================================================
% Tutorial 2 - Gráficos 2D
% =====================================================

% limpa a memória, a tela, e fecha todas as janelas
clearvars; clc; close all;

% define vetor t, que vai de zero a 4pi com passo pi/50
t=0:pi/50:4*pi;

% cria vetor com o seno dos valores de t
% note que o vetor y1 tem a mesma dimensao de t
y1=sin(t);

% cria vetor com o cosseno dos valores de t
% note que o vetor y2 tem a mesma dimensao de t
y2=cos(t);

% diversos argumentos do comando PLOT são utilizados para a
% controlar a aparência do gráfico; alguns são empregados abaixo
% Color - define a cor da curva (k-black, r-red, b-blue, m-magenta, etc)
% Linewidth - define a espessura da linha em pixels
% Linestyle - define o estilo da linha ('-' contínua, '--'-tracejada, etc)
plot(t,y1,'Color','k','LineStyle','--','LineWidth',2);

% o comando HOLD ON impede que a curva atual seja apagada do gráfico
% quando o próximo comando de plotagem for utilizado; ou seja,
% o comando HOLD ON permite exibir diversas curvas no mesmo gráfico
hold on;

% exibe as linhas de grade
grid on;

% plota y2
plot(t,y2,'Color','r','LineWidth',2);

% define o tamanho da fonte
% set - comando que define propriedades de objetos gráficos
% gca - get current axis -> retorna um handle para o eixo do gráfico
set(gca,'FontSize',18);

% define os limites do eixo horizontal do gráfico
% o comando XLIM([xi xf]) recebe como argumento um vetor com 2 elementos
% xi - valor inicial (0, que é o primeiro elemento do vetor t)
% xf - valor final (4*pi, que é o últimno elemento do vetor t)
% o comando LENGTH retorna o comprimento (número de elementos) do vetor t
% logo t(length(t)) retorna o último elemento do vetor t
xlim([t(1) t(length(t))]);

% define rótulos para os eixos x e y
xlabel('arco (radianos)');
ylabel('f(x)');

% define a legenda do gráfico
% note que os nomes na legenda devem ser definidos na mesma ordem
% em que as curvas foram plotadas (neste exemplo, primeiro o seno e depois o cosseno)
legend('seno','cosseno');

% abre nova janela para plotagem
figure;

% define vetor x de 0.01 a 10 com passo 1/100
x=0.01:.01:10;

% utilizaremos agora o comando SUBPLOT para exibir subgráficos na mesma janela
% SUBPLOT(M,N,i) - cria uma janela para MxN subgráficos (M linhas e N colunas)
% "i" é o índice do subgráfico atual
subplot(2,2,1); % 2 x 2 subgráficos; plotando o primeiro (i=1)
plot(x,log10(x),'Color','k','LineWidth',2);
set(gca,'FontSize',18);
grid on;
xlabel('x');
ylabel('y=log10(x)');

% o comando SEMILOGY exibe o gráfico com escala vertical logarítmica
% note que é essential utilizar o comando GRID ON para visualizar a escala logarítmica
subplot(2,2,2); % note que o índice agora é 2 (segundo subgráfico)
x=1.01:0.01:10;
semilogy(x,log10(x),'Color','k','LineWidth',2);
set(gca,'FontSize',18);
grid on;
xlabel('x');
ylabel('y=log10(x)');

% agora no mesmo gráfico exibiremos várias curvas exponenciais
% variando o valor da constante "a", onde y=exp(a*x)
x=-10:0.01:10;
subplot(2,2,3);
for a=-0.2:.1:0.2
  plot(x,exp(a*x));
  hold on; grid on;
end;
set(gca,'FontSize',18);
xlabel('x');
ylabel('y=exp(a*x)');
legend('a=-0.2','a=-0.1','a=0','a=+0.1','a=+0.2');

% agora no mesmo gráfico exibiremos a curva logarítmica (base natural),
% a função exponencial e a função identidade
% como y=log(x) e y=exp(x) são funções inversas, seus gráficos são simétricos
% em relação à reta y=x
subplot(2,2,4);
x=0.01:0.01:2;
plot(x,log(x),'Color','b','LineStyle','-','LineWidth',2);
hold on;
x=-2:0.01:2;
plot(x,exp(x),'Color','r','LineStyle','-','LineWidth',2);
plot(x,x,'Color','k','LineStyle','--','LineWidth',2);
set(gca,'FontSize',18);
xlim([-2 2]); ylim([-2 2]); grid on;
% define a relação entre as escalas dos eixos (todos com a mesma escala)
pbaspect([1 1 1]);

figure;

% gráfico polar - lemniscata
% r^2=4*cos(2t)
% cos(2t)>=0 -> -pi/2<=2t<=pi/2
% -pi/4<=t<=pi/4

t=-45:.1:45;
a=20;

rp=a*sqrt(cosd(2*t));
rn=-a*sqrt(cosd(2*t));

xp = rp.*cosd(2*t);
yp = rp.*sind(2*t);

xn = rn.*cosd(2*t);
yn = rn.*sind(2*t);

scatter(xp,yp,'k','.');
hold on;
scatter(xn,yn,'k','.');
pbaspect([1 1 1]);
grid on;
ylim([-a a]);
