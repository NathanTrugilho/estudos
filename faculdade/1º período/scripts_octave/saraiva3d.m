%=====================================================
% CEFET-RJ Campus Petropolis
% Faculdade de Engenharia de Computação
% GCOM1001PE - Introdução à Engenharia - 2022/1
% Prof. Rafael Saraiva Campos
% =====================================================
% Tutorial 3 - Gráficos 3D
% =====================================================
clearvars; clc; close all;

% PLOT3(X,Y,Z)
% grafico tridimensionais de curvas
% espirais 3D na forma paramétrica
t=0:pi/50:8*pi;

subplot(1,2,1);
plot3(sin(t),cos(t),t,'LineWidth',2);
grid on;
xlabel('x'); ylabel('y'); zlabel('z');
view([45 10]); % define visada do gráfico (azimute e elevação)

subplot(1,2,2);
plot3(t.*sin(t),t.*cos(t),t,'LineWidth',2);
grid on; xlabel('x'); ylabel('y'); zlabel('z');
view([45 10]); % define visada do gráfico (azimute e elevação)

% SCATTER3(X,Y,Z)  plota pontos no espaco
figure; % abre nova janela
[x,y]=meshgrid(-5:0.5:5);
scatter3(x,y,sqrt(x.^2+y.^2));

% SURF(X,Y,Z) - grafico de superficies
figure;
[x,y] = meshgrid(-5:.5:5); % cria matriz de pontos (x,y)

% cria um cell array com 4 elementos
% cada elemento é uma matriz contendo os valores z=f(x,y)
% para maiores informações sobre cell arrays, consulte o tutorial 4
z{1} = sqrt(x.^2+y.^2); % cone
z{2} = x.^2+y.^2; % parabolóide de revolução
z{3} = x.^2-y.^2; % parabolóide hiperbólico
z{4} = x+y; % plano

% cell array contendo os títulos dos gráficos
TITULO = {'cone','parabolóide de revolução','parabolóide hiperbólico','plano'};

for i=1:4
  subplot(2,2,i);
  surf(x,y,z{i});
  xlabel('x'); ylabel('y'); zlabel('z');
  title(TITULO{i});
end;

% CONTOUR(Z) - exibe as curvas de nível da superfície representada pela matriz Z
figure;
for i=1:4
  subplot(2,2,i);
  contour(x,y,z{i});
  xlabel('x'); ylabel('y'); zlabel('z');
  title(TITULO{i});
  pbaspect([1 1 1]);
end;

% Elipsoide de Revolução
% equação geral: (x-x0)^2/a^2 + (y-y0)^2/b^2+(z-z0)^2/c^2
% (x0,y0,z0) - coordenadas do centro
% a,b,c - comprimento dos semi-eixos x,y,z
figure;

subplot(1,2,1);
a=2; b=4; c=2;
x0 = 0; y0=0; z0=0;
ellipsoid(x0,y0,z0,a,b,c);
pbaspect([a b c]);
title('elipsóide');

% obtém-se uma esfera fazendo a=b=c
subplot(1,2,2);
a=1; b=1; c=1; % neste caso, uma esfera de raio 1
ellipsoid(x0,y0,z0,a,b,c);
pbaspect([a b c]);
title('esfera');
