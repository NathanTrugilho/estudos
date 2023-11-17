;==============================================================================
; ZONA 0: compilar e rodar programa
; Linux:        ./p3as-linux nathan.as; java -jar p3sim.jar nathan.exe
; Windows:      .\p3as-win.exe .\nathan.as ; java -jar .\p3sim.jar .\nathan.exe
;
;           Lembrar de definir uma IVAD4 para iniciar o jogo !!!!!!!!
;==============================================================================

;------------------------------------------------------------------------------
; ZONA I: Definicao de constantes
;         Pseudo-instrucao : EQU
;------------------------------------------------------------------------------
; Constantes do Sistema
;------------------------------------------------------------------------------

CR              EQU     0Ah
TIMER_COUNTER   EQU     FFF6h
ACTIVATE_TIMER  EQU     FFF7h
FIM_TEXTO       EQU     '@'
IO_READ         EQU     FFFFh
IO_WRITE        EQU     FFFEh
IO_STATUS       EQU     FFFDh
INITIAL_SP      EQU     FDFFh
CURSOR		    EQU     FFFCh
CURSOR_INIT		EQU		FFFFh
ROW_POSITION	EQU		0d
COL_POSITION	EQU		0d
ROW_SHIFT		EQU		8d
COLUMN_SHIFT	EQU		8d
;------------------------------------------------------------------------------
; Constantes do jogo
;------------------------------------------------------------------------------

BASE_ASCII                   EQU     48d
 
COLUNA_CENTENA_PONTOS        EQU     75d
COLUNA_COMECO_BARRA          EQU     34d
COLUNA_DEZENA_PONTOS         EQU     76d
COLUNA_MENSAGEM_FIM_JOGO     EQU     28d
COLUNA_UNIDADE_PONTOS        EQU     77d
COORDENADA_INICIAL_X_BOLA    EQU     40d
COORDENADA_INICIAL_Y_BOLA    EQU     17d
 
LINHA_LABEL_MENU             EQU      1d
LINHA_MENSAGEM_FIM_JOGO      EQU     18d
 
POSICAO_LINHA_BARRA          EQU     21d
 
QUANTIDADE_BLOCOS            EQU     278d
QUANTIDADE_CARACTERES_LINHA  EQU     80d
 
TAMANHO_BARRA                EQU     12d     ;Deve ser um múltiplo de 3
TEMPO_DE_ATUALIZACAO         EQU      1d

;------------------------------------------------------------------------------
; ZONA II: definicao de variaveis
;          Pseudo-instrucoes : WORD - palavra (16 bits)
;                              STR  - sequencia de caracteres (cada ocupa 1 palavra: 16 bits).
;          Cada caracter ocupa 1 palavra
;------------------------------------------------------------------------------

                ORIG    8000h
argumento_char_Printchar           WORD    0d
argumento_pos_coluna_Printbarra    WORD    0d
argumento_pos_coluna_Printchar     WORD    0d
argumento_pos_coluna_Printstr      WORD    0d
argumento_pos_linha_Printbarra     WORD    0d
argumento_pos_linha_Printchar      WORD    0d
argumento_pos_linha_Printstr       WORD    0d
argumento_string_Printmenu         WORD    0d
argumento_string_Printstr          WORD    0d

bola                               WORD    'O'   

mensagem_derrota                   STR     'Voce perdeu! Shame on you ', FIM_TEXTO
mensagem_vitoria                   STR     'Voce ganhou, que legal! :P', FIM_TEXTO
movimentacao_X_bola                WORD    0d
movimentacao_Y_bola                WORD    1d

posicao_anterior_X_bola            WORD    0d
posicao_anterior_Y_bola            WORD    0d
posicao_atual_X_bola               WORD    COORDENADA_INICIAL_X_BOLA
posicao_atual_Y_bola               WORD    COORDENADA_INICIAL_Y_BOLA 
posicao_fim_barra                  WORD    0d
posicao_inicio_barra               WORD    0d
posicao_mostrador_vidas            WORD    17d
    
quantidade_blocos_destruidos       WORD    0d

tamanho_pedaco_barra               WORD    0d

vidas                              WORD    3d

Line1           STR     '+==================+=============================================+=============+'
Line2           STR     '| Bolas: O - O - O |      O melhor trabalho de arquitetura       | Pontos: 000 |'
Line3           STR     '+==================+=============================================+=============+'
Line4           STR     '|                                                                              |'
Line5           STR     '|                      #####                        #####                      |'
Line6           STR     '|                           ##                    ##                           |'
Line7           STR     '|                           ########################                           |'
Line8           STR     '|                         ############################                         |'
Line9           STR     '|                       ########  ############  ########                       |'
Line10          STR     '|                       ########  ############  ########                       |'
Line11          STR     '|                     ####################################                     |'  ;78 espaços
Line12          STR     '|                     ############   ######   ############                     |'
Line13          STR     '|                     ############     ##     ############                     |'
Line14          STR     '|                     ##   ##########################   ##                     |'
Line15          STR     '|                     ##   ##                      ##   ##                     |'
Line16          STR     '|                     ##   #####                #####   ##                     |'
Line17          STR     '|                            ######          ######                            |'
Line18          STR     '|                                                                              |'
Line19          STR     '|                                                                              |'
Line20          STR     '|                                                                              |'
Line21          STR     '|                                                                              |'
Line22          STR     '|                                                                              |'
Line23          STR     '|                                                                              |'
Line24          STR     '\______________________________________________________________________________/', FIM_TEXTO

;------------------------------------------------------------------------------
; ZONA III: definicao de tabela de interrupções
;------------------------------------------------------------------------------
                ORIG    FE00h
INT0            WORD    movimenta_barra_esquerda
INT1            WORD    movimenta_barra_direita
INT2            WORD    movimento_longo_barra_esquerda
INT3            WORD    movimento_longo_barra_direita
INT4            WORD    StartGame

                ORIG    FE0Fh
INT15           WORD    Timer

;------------------------------------------------------------------------------
; ZONA IV: codigo
;        conjunto de instrucoes Assembly, ordenadas de forma a realizar
;        as funcoes pretendidas
;------------------------------------------------------------------------------
                ORIG    0000h
                JMP     Main

;-----------------------------------------------------------------------------------------
; Função movimenta_barra_esquerda - O nome é bem óbvio, não preciso explicar
;                                  Usar o caractere 'a' em IVAD0 no simulador
;-----------------------------------------------------------------------------------------

movimenta_barra_esquerda:  PUSH R1
        
        ; Faz a verificação para movimentar -------------------------

            MOV R1, M[posicao_inicio_barra]
            CMP R1, 1
            JMP.Z final_if_movimenta_barra_esquerda

            MOV R1, POSICAO_LINHA_BARRA
            MOV M[argumento_pos_linha_Printchar], R1

        ; Parte mais à direita da barra -----------------------------

            MOV R1, M[posicao_fim_barra]
            MOV M[argumento_pos_coluna_Printchar], R1
            DEC M[posicao_fim_barra]
            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

        ; Parte mais à esquerda da barra ----------------------------

            DEC M[posicao_inicio_barra]
            MOV R1, M[posicao_inicio_barra]
            MOV M[argumento_pos_coluna_Printchar], R1
            MOV R1, '='
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            final_if_movimenta_barra_esquerda: NOP
            POP R1
            RTI

;-----------------------------------------------------------------------------------------
; Função movimenta_barra_direita - O nome é bem óbvio, não preciso explicar
;                                  Usar o caractere 'd' em IVAD1 no simulador
;-----------------------------------------------------------------------------------------

movimenta_barra_direita:  PUSH R1
        
        ; Faz a verificação para movimentar -------------------------

            MOV R1, M[posicao_fim_barra]
            CMP R1, 78
            JMP.Z final_if_movimenta_barra_direita

            MOV R1, POSICAO_LINHA_BARRA
            MOV M[argumento_pos_linha_Printchar], R1

        ; Parte mais à esquerda da barra ----------------------------

            MOV R1, M[posicao_inicio_barra]
            INC M[posicao_inicio_barra]
            MOV M[argumento_pos_coluna_Printchar], R1
            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

        ; Parte mais à direita da barra -----------------------------

            MOV R1, M[posicao_fim_barra]
            INC M[posicao_fim_barra]
            MOV M[argumento_pos_coluna_Printchar], R1
            INC M[argumento_pos_coluna_Printchar]
            MOV R1, '='
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            final_if_movimenta_barra_direita: NOP
            POP R1
            RTI

;-----------------------------------------------------------------------------------------
; função movimento_longo_barra_esquerda - Movimenta 3 colunas por vez
;                                         Usar o caractere 'q' em IVAD2 no simulador
;-----------------------------------------------------------------------------------------

movimento_longo_barra_esquerda: PUSH R1
        
        ; Faz a verificação para movimentar -------------------------

            MOV R1, M[posicao_inicio_barra]
            CMP R1, 3
            JMP.NP final_if_movimento_longo_barra_esquerda

            MOV R1, POSICAO_LINHA_BARRA
            MOV M[argumento_pos_linha_Printchar], R1

        ; Parte mais à direita da barra -----------------------------

            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            MOV R1, M[posicao_fim_barra]
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar
            DEC R1
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar
            DEC R1
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar

        ; Parte mais à esquerda da barra ----------------------------

            MOV R1, '='
            MOV M[argumento_char_Printchar], R1
            MOV R1, M[posicao_inicio_barra]
            DEC R1
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar
            DEC R1
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar
            DEC R1
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar

        ; Ajusta as novas posições do incício e do fim da barra -----

            MOV R1, M[posicao_fim_barra]
            SUB R1, 3
            MOV M[posicao_fim_barra], R1
            MOV R1, M[posicao_inicio_barra]
            SUB R1, 3
            MOV M[posicao_inicio_barra], R1

            final_if_movimento_longo_barra_esquerda: NOP
            POP R1
            RTI

;-----------------------------------------------------------------------------------------
; função movimento_longo_barra_direita - Movimenta 3 colunas por vez
;                                        Usar o caractere 'e' em IVAD3 no simulador
;-----------------------------------------------------------------------------------------

movimento_longo_barra_direita: PUSH R1

        ; Faz a verificação para movimentar -------------------------

            MOV R1, M[posicao_fim_barra]
            CMP R1, 76
            JMP.NN final_if_movimento_longo_barra_direita

            MOV R1, POSICAO_LINHA_BARRA
            MOV M[argumento_pos_linha_Printchar], R1

        ; Parte mais à direita da barra -----------------------------

            MOV R1, '='
            MOV M[argumento_char_Printchar], R1
            MOV R1, M[posicao_fim_barra]
            INC R1
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar
            INC R1
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar
            INC R1
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar

        ; Parte mais à esquerda da barra ----------------------------

            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            MOV R1, M[posicao_inicio_barra]
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar
            INC R1
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar
            INC R1
            MOV M[argumento_pos_coluna_Printchar], R1
            CALL Printchar

        ; Ajusta as novas posições do incício e do fim da barra -----

            MOV R1, M[posicao_fim_barra]
            ADD R1, 3
            MOV M[posicao_fim_barra], R1

            MOV R1, M[posicao_inicio_barra]
            ADD R1, 3
            MOV M[posicao_inicio_barra], R1

            final_if_movimento_longo_barra_direita: NOP
            POP R1
            RTI

;-----------------------------------------------------------------------------------------
; Função Printchar - Imprime um caractere
;
; Recebe como parâmetros: a posição da linha guardada em "argumento_pos_linha_Printchar"
;                         a posição da coluna guardada em "argumento_pos_coluna_Printchar"
;                         o endereço do caractere guardado em "argumento_char_Printchar"
;-----------------------------------------------------------------------------------------

Printchar:  PUSH R1
            PUSH R2

            MOV R2, M[argumento_pos_linha_Printchar]
            SHL R2, 8d
            MOV R1, M[argumento_pos_coluna_Printchar] 
            OR R2, R1
            MOV R1, M[argumento_char_Printchar] 
            MOV M[CURSOR], R2
            MOV M[IO_WRITE], R1

            POP R2
            POP R1
            RET

;-----------------------------------------------------------------------------------------
; Função Printstr - Imprime uma string
;
; Recebe como parâmetros: a posição da linha guardada em "argumento_pos_linha_Printstr"
;                         a posição da coluna guardada em "argumento_pos_coluna_Printstr"
;                         o endereço da string guardado em "argumento_string_Printstr"
;-----------------------------------------------------------------------------------------

Printstr:   PUSH R1
            PUSH R2
            PUSH R3

            MOV R2, M[argumento_pos_linha_Printstr]
            SHL R2, 8d
            MOV R1, M[argumento_pos_coluna_Printstr] 
            OR R2, R1
            MOV R3, M[argumento_string_Printstr] 
            MOV R1, M[R3]

            loop_Printstr:  CMP R1, FIM_TEXTO
            JMP.Z fim_loop_Printstr
            MOV M[CURSOR], R2
            MOV M[IO_WRITE], R1
            INC R2
            INC R3
            MOV R1, M[R3]
            JMP loop_Printstr

            fim_loop_Printstr: NOP

            POP R3
            POP R2
            POP R1
            RET

;-----------------------------------------------------------------------------------------
; Função Printbarra - Imprime a barra com a posição especificada pelas 
; constantes "POSICAO_LINHA_BARRA", "COLUNA_COMECO_BARRA" e com o tamanho definido 
; em "TAMANHO_BARRA"
;
; Recebe como parâmetros: a posição da linha guardada em "argumento_pos_linha_Printbarra"
;                         a posição da coluna guardada em "argumento_pos_coluna_Printbarra"
;-----------------------------------------------------------------------------------------

Printbarra: PUSH R1
            PUSH R2
            PUSH R3

        ; Define a posição do inicio e fim da barra -----------

            MOV R1, COLUNA_COMECO_BARRA
            MOV M[posicao_inicio_barra], R1
            ADD R1, TAMANHO_BARRA
            DEC R1
            MOV M[posicao_fim_barra], R1  

        ; Calcula a posição de impressão ----------------------

            MOV R3, POSICAO_LINHA_BARRA
            SHL R3, 8d
            MOV R2, COLUNA_COMECO_BARRA
            OR R3, R2
            MOV R2, TAMANHO_BARRA
            MOV R1, '='

        ; Faz a impressão -------------------------------------
        
            loop_Printbarra: CMP R2, R0
            JMP.Z fim_loop_Printbarra
            MOV M[CURSOR], R3
            MOV M[IO_WRITE], R1
            DEC R2
            INC R3
            JMP loop_Printbarra
            fim_loop_Printbarra: NOP
            
            MOV R1, TAMANHO_BARRA
            MOV R2, 3
            DIV R1, R2
            DEC R1
            MOV M[tamanho_pedaco_barra], R1

            POP R3
            POP R2
            POP R1
            RET

;------------------------------------------------------------------------------------------------
; Função Limpabarra - nome óbvio, não é mesmo? De qualquer jeito, serve para limpar a barra da   
; tela quando o jogador perde uma vida.
;------------------------------------------------------------------------------------------------

Limpabarra: PUSH R1
            PUSH R2
            PUSH R3

        ; Calcula a posição do cursor --------------------------

            MOV R3, POSICAO_LINHA_BARRA
            SHL R3, 8d
            MOV R2, M[posicao_inicio_barra]
            OR R3, R2
            MOV R2, TAMANHO_BARRA
            MOV R1, ' '

        ; Imprime espaços para limpar a barra ------------------
        
            loop_Limpabarra: CMP R2, R0
            JMP.Z fim_loop_Limpabarra
            MOV M[CURSOR], R3
            MOV M[IO_WRITE], R1
            DEC R2
            INC R3
            JMP loop_Limpabarra
            fim_loop_Limpabarra: NOP

            POP R3
            POP R2
            POP R1
            RET

;-------------------------------------------------------------------------------
; Função Printmenu - Imprime a janela do menu do jogo 
;
; Recebe como parâmetro: o endereço da string guardada em "argumento_string_Printmenu"                       
;-------------------------------------------------------------------------------

Printmenu:  PUSH R1
            PUSH R2
            PUSH R3
            PUSH R4
            PUSH R5

            MOV R5, Line1               
            MOV M[argumento_string_Printmenu], R5
            MOV R1, M[R5] 
            MOV R2, FIM_TEXTO
            MOV R3, R0 ; POSIÇÃO DE PRINT  
            MOV R4, R0 ; CONTADOR

        ; Contador para saber quando deve-se pular para a próxima linha -----------

            loop_Printmenu: CMP R1, R2
            JMP.Z fim_loop_Printmenu
            CMP R4, 80

        ; Faz os ajustes necessários quando vou para a próxima linha --------------

            JMP.NZ proxima_linha_Printmenu   ; if zero, next line
            SUB R3, R4
            MOV R4, 1
            SHL R4, 8
            ADD R3, R4
            MOV R4, R0
            proxima_linha_Printmenu: MOV M[CURSOR], R3

        ; Imprime o conteúdo ------------------------------------------------------

            MOV M[IO_WRITE], R1
            INC R3
            INC R4
            INC R5
            MOV R1, M[R5]
            JMP loop_Printmenu
            
            fim_loop_Printmenu: NOP
            
            POP R5
            POP R4
            POP R3
            POP R2
            POP R1
            RET

;-------------------------------------------------------------------------------
; Função DisplayPontos - Função para atualizar o contador de pontos                    
;-------------------------------------------------------------------------------

DisplayPontos:  PUSH R1
                PUSH R2

                MOV R1, LINHA_LABEL_MENU
                MOV M[argumento_pos_linha_Printchar], R1
                MOV R1, COLUNA_CENTENA_PONTOS
                MOV M[argumento_pos_coluna_Printchar], R1
                MOV R2, M[quantidade_blocos_destruidos]

                MOV R1, 100
                DIV R2, R1
                ADD R2, BASE_ASCII
                MOV M[argumento_char_Printchar], R2
                CALL Printchar

                MOV R2, COLUNA_DEZENA_PONTOS
                MOV M[argumento_pos_coluna_Printchar], R2
                MOV R2, 10
                DIV R1, R2
                ADD R1, BASE_ASCII
                MOV M[argumento_char_Printchar], R1
                CALL Printchar

                MOV R1, COLUNA_UNIDADE_PONTOS
                MOV M[argumento_pos_coluna_Printchar], R1
                MOV R1, 1
                DIV R2, R1
                ADD R2, BASE_ASCII
                MOV M[argumento_char_Printchar], R2
                CALL Printchar

                POP R2
                POP R1
                RET

;-------------------------------------------------------------------------------
; Função SetTimer - Função que configura uma interrupção                     
;-------------------------------------------------------------------------------

SetTimer:   PUSH R1

            MOV R1, TEMPO_DE_ATUALIZACAO
            MOV M[ TIMER_COUNTER ], R1
            MOV R1, 1d 
            MOV M[ ACTIVATE_TIMER ], R1   

            POP R1
            RET

;-------------------------------------------------------------------------------
; Função Timer - Função que inicia o jogo                    
;-------------------------------------------------------------------------------
Timer:      PUSH R1
            PUSH R2
            
; Faz o processo de movimento da bola com base nas "direções" que ela vai seguir. Os argumentos de direção 
; estão guardados em "movimentacao_X_bola" e "movimentacao_Y_bola"

            MOV R1, M[posicao_atual_X_bola]
            MOV M[posicao_anterior_X_bola], R1
            ADD R1, M[movimentacao_X_bola]
            MOV M[posicao_atual_X_bola], R1

            MOV R2, M[posicao_atual_Y_bola]
            MOV M[posicao_anterior_Y_bola], R2
            ADD R2, M[movimentacao_Y_bola]
            MOV M[posicao_atual_Y_bola], R2

; Detecta a colisão com os blocos ******************************************
;   
;   #
;   #
;   # O
;   #
;
;   O tipo de colisão (vertical, horizontal, diagonal) é dado pela verificação na memória com base nas    
;   posições de memória (posicao_atual_X_bola/posicao_anterior_X_bola e posicao_atual_Y_bola/posicao_anterior_Y_bola)
;
    ; Colisões verticais --------------------------------------------------------

            MOV R1, QUANTIDADE_CARACTERES_LINHA
            MOV R2, M[posicao_atual_Y_bola]
            MUL R1, R2
            MOV R1, M[posicao_anterior_X_bola]
            ADD R1, R2
            MOV R2, Line1
            ADD R1, R2
            MOV R2, M[R1]

            CMP R2, '#'
            JMP.NZ fim_if_colisao_bloco_vertical

            INC M[quantidade_blocos_destruidos]
            MOV M[R1], R0
            MOV R2, M[posicao_atual_Y_bola]
            MOV R1, M[posicao_anterior_X_bola]
            MOV M[argumento_pos_linha_Printchar], R2
            MOV M[argumento_pos_coluna_Printchar], R1
            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            MOV R2, M[movimentacao_Y_bola]
            MOV R1, -1
            MUL R2, R1
            MOV M[movimentacao_Y_bola], R1

            MOV R2, M[posicao_anterior_Y_bola]
            MOV M[posicao_atual_Y_bola], R2
            ADD R2, M[movimentacao_Y_bola]
            MOV M[posicao_atual_Y_bola], R2
        
        ; Chama a função do mostrador de pontos ----------------------------------

            CALL DisplayPontos
            
            fim_if_colisao_bloco_vertical: NOP

    ; Colisões horizontais --------------------------------------------------------

            MOV R1, QUANTIDADE_CARACTERES_LINHA
            MOV R2, M[posicao_anterior_Y_bola]
            MUL R1, R2
            MOV R1, M[posicao_atual_X_bola]
            ADD R1, R2
            MOV R2, Line1
            ADD R1, R2
            MOV R2, M[R1]

            CMP R2, '#'
            JMP.NZ fim_if_colisao_bloco_horizontal

            INC M[quantidade_blocos_destruidos]
            MOV M[R1], R0
            MOV R2, M[posicao_anterior_Y_bola]
            MOV R1, M[posicao_atual_X_bola]
            MOV M[argumento_pos_linha_Printchar], R2
            MOV M[argumento_pos_coluna_Printchar], R1
            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            MOV R2, M[movimentacao_X_bola]
            MOV R1, -1
            MUL R2, R1
            MOV M[movimentacao_X_bola], R1

            MOV R2, M[posicao_anterior_X_bola]
            MOV M[posicao_atual_X_bola], R2
            ADD R2, M[movimentacao_X_bola]
            MOV M[posicao_atual_X_bola], R2

        ; Chama a função do mostrador de pontos ----------------------------------

            CALL DisplayPontos
            
            fim_if_colisao_bloco_horizontal: NOP

    ; Colisões diagonais --------------------------------------------------------

            MOV R1, QUANTIDADE_CARACTERES_LINHA
            MOV R2, M[posicao_atual_Y_bola]
            MUL R1, R2
            MOV R1, M[posicao_atual_X_bola]
            ADD R1, R2
            MOV R2, Line1
            ADD R1, R2
            MOV R2, M[R1]

            CMP R2, '#'
            JMP.NZ fim_if_colisao_bloco_diagonal

            INC M[quantidade_blocos_destruidos]
            MOV M[R1], R0
            MOV R2, M[posicao_atual_Y_bola]
            MOV R1, M[posicao_atual_X_bola]
            MOV M[argumento_pos_linha_Printchar], R2
            MOV M[argumento_pos_coluna_Printchar], R1
            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            MOV R2, M[movimentacao_X_bola]
            MOV R1, -1
            MUL R2, R1
            MOV M[movimentacao_X_bola], R1

            MOV R2, M[movimentacao_Y_bola]
            MOV R1, -1
            MUL R2, R1
            MOV M[movimentacao_Y_bola], R1

            MOV R2, M[posicao_anterior_X_bola]
            MOV M[posicao_atual_X_bola], R2
            ADD R2, M[movimentacao_X_bola]
            MOV M[posicao_atual_X_bola], R2

            MOV R2, M[posicao_anterior_Y_bola]
            MOV M[posicao_atual_Y_bola], R2
            ADD R2, M[movimentacao_Y_bola]
            MOV M[posicao_atual_Y_bola], R2

        ; Chama a função do mostrador de pontos ----------------------------------

            CALL DisplayPontos
            
            fim_if_colisao_bloco_diagonal: NOP

        ; Verifica se o jogador destruiu todos os blocos e, por isso, ganhou -----

            MOV R1, QUANTIDADE_BLOCOS
            MOV R2, M[quantidade_blocos_destruidos]
            CMP R2, R1
            JMP.NZ continua_jogo_not_ganhador

            MOV R1, LINHA_MENSAGEM_FIM_JOGO
            MOV M[argumento_pos_linha_Printstr], R1
            MOV R2, COLUNA_MENSAGEM_FIM_JOGO
            MOV M[argumento_pos_coluna_Printstr], R2
            MOV R1, mensagem_vitoria
            MOV M[argumento_string_Printstr], R1
            CALL Printstr
            JMP Halt

            continua_jogo_not_ganhador: NOP

; Verifica se a bola bateu na barra e faz o cálculo de sua nova direção caso verdade ******

            MOV R1, M[posicao_atual_Y_bola]
            CMP R1, POSICAO_LINHA_BARRA
            JMP.NZ fim_if_colisao_barra

            MOV R2, M[posicao_atual_X_bola]
            CMP R2, M[posicao_inicio_barra]
            JMP.N fim_if_colisao_barra
            MOV R1, M[posicao_fim_barra]
            CMP R2, R1
            JMP.P fim_if_colisao_barra

            ; Extremidade esquerda da barra ------------------------------

            MOV R1, M[posicao_anterior_X_bola]
            MOV R2, M[posicao_inicio_barra]
            ADD R2, M[tamanho_pedaco_barra]
            CMP R1, R2
            JMP.NN fim_if_colisao_esquerda_barra

            MOV R1, M[movimentacao_X_bola]
            DEC R1
            CMP R1, -2 ; Preciso fazer a correção para a bola não se mover dois pixels por vez
            JMP.NZ fim_if_correcao_esquerda_barra
            INC R1
            fim_if_correcao_esquerda_barra: NOP
            MOV M[movimentacao_X_bola], R1

            MOV R1, M[posicao_anterior_X_bola]
            MOV M[argumento_pos_coluna_Printchar], R1
            MOV R2, M[posicao_anterior_Y_bola]
            MOV M[argumento_pos_linha_Printchar], R2
            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            fim_if_colisao_esquerda_barra: NOP

            ; Extremidade direita da barra ------------------------------

            MOV R1, M[posicao_anterior_X_bola]
            MOV R2, M[posicao_fim_barra]
            SUB R2, M[tamanho_pedaco_barra]
            CMP R1, R2
            JMP.NP fim_if_colisao_direita_barra

            MOV R1, M[movimentacao_X_bola]
            INC R1
            CMP R1, 2 ; Preciso fazer a correção para a bola não se mover dois pixels por vez
            JMP.NZ fim_if_correcao_direita_barra
            DEC R1
            fim_if_correcao_direita_barra: NOP
            MOV M[movimentacao_X_bola], R1

            MOV R2, M[posicao_anterior_Y_bola]
            MOV M[argumento_pos_linha_Printchar], R2
            MOV R1, M[posicao_anterior_X_bola]
            MOV M[argumento_pos_coluna_Printchar], R1
            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            fim_if_colisao_direita_barra: NOP

            ; Caso geral de colisão (bater no meio da barra)---------------

            MOV R1, -1 
            MOV M[movimentacao_Y_bola], R1

            MOV R1, M[posicao_anterior_X_bola]
            MOV M[posicao_atual_X_bola], R1
            MOV R1, M[posicao_anterior_Y_bola]
            MOV M[posicao_atual_Y_bola], R1
            MOV R1, M[posicao_atual_X_bola]
            ADD R1, M[movimentacao_X_bola]
            MOV M[posicao_atual_X_bola], R1

            MOV R2, M[posicao_atual_Y_bola]
            MOV M[posicao_anterior_Y_bola], R2
            ADD R2, M[movimentacao_Y_bola]
            MOV M[posicao_atual_Y_bola], R2

        ; Caso não haja colisões, o código vem para cá ---------------------
        
            fim_if_colisao_barra: NOP

; Detecta a colisão com as bordas ******************************************

    ; Borda esquerda -------------------------------------------------------

            MOV R1, M[posicao_atual_X_bola]
            CMP R1, 0
            JMP.NZ fim_if_colisao_parede_esquerda
            MOV R1, 1
            MOV M[movimentacao_X_bola], R1
            MOV R1, M[posicao_anterior_X_bola]
            ADD R1, M[movimentacao_X_bola]
            MOV M[posicao_atual_X_bola], R1
            MOV R1, M[posicao_anterior_Y_bola]
            ADD R1, M[movimentacao_Y_bola]
            MOV M[posicao_atual_Y_bola], R1

            fim_if_colisao_parede_esquerda: NOP
    
    ; Borda direita -------------------------------------------------------

            MOV R1, M[posicao_atual_X_bola]
            CMP R1, 79
            JMP.NZ fim_if_colisao_parede_direita
            MOV R1, -1
            MOV M[movimentacao_X_bola], R1
            MOV R1, M[posicao_anterior_X_bola]
            ADD R1, M[movimentacao_X_bola]
            MOV M[posicao_atual_X_bola], R1
            MOV R1, M[posicao_anterior_Y_bola]
            ADD R1, M[movimentacao_Y_bola]
            MOV M[posicao_atual_Y_bola], R1

            fim_if_colisao_parede_direita: NOP

    ; Teto ----------------------------------------------------------------
                                                                
            MOV R1, M[posicao_atual_Y_bola]                      
            CMP R1, 2
            JMP.NZ fim_if_colisao_teto
            MOV R1, 1
            MOV M[movimentacao_Y_bola], R1
            MOV R1, M[posicao_anterior_X_bola]
            ADD R1, M[movimentacao_X_bola]
            MOV M[posicao_atual_X_bola], R1
            MOV R1, M[posicao_anterior_Y_bola]
            ADD R1, M[movimentacao_Y_bola]
            MOV M[posicao_atual_Y_bola], R1

            fim_if_colisao_teto: NOP

    ; Chao --------------------------------------------------------------

            MOV R1, M[posicao_atual_Y_bola]
            ADD R1, M[movimentacao_Y_bola]
            CMP R1, 24
            JMP.NZ fim_if_colisao_chao

            CMP R0, M[vidas]
            JMP.NZ continua_jogo

            MOV R1, LINHA_MENSAGEM_FIM_JOGO
            MOV M[argumento_pos_linha_Printstr], R1
            MOV R2, COLUNA_MENSAGEM_FIM_JOGO
            MOV M[argumento_pos_coluna_Printstr], R2
            MOV R1, mensagem_derrota
            MOV M[argumento_string_Printstr], R1
            CALL Printstr
            JMP Halt

            continua_jogo: NOP

            DEC M[vidas]

        ; Apaga as as vidas (bolas) mostradas ao display -----------------

            MOV R1, LINHA_LABEL_MENU
            MOV M[argumento_pos_linha_Printchar], R1
            MOV R2, M[posicao_mostrador_vidas]
            MOV M[argumento_pos_coluna_Printchar], R2
            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            MOV R1, 4 ; O número quatro representa a quantidade de espaços que separa uma bola do índice da outra
            SUB M[posicao_mostrador_vidas], R1

        ; Reinicia o jogo após usar uma vida -----------------------------

            MOV M[movimentacao_X_bola], R0
            MOV R1, COORDENADA_INICIAL_Y_BOLA
            MOV M[posicao_atual_Y_bola], R1
            MOV M[argumento_pos_linha_Printchar], R1 
            MOV R1, COORDENADA_INICIAL_X_BOLA
            MOV M[posicao_atual_X_bola], R1
            MOV M[argumento_pos_coluna_Printchar], R1      
            MOV R1, bola   
            MOV R1, M[R1] 
            MOV M[argumento_char_Printchar], R1   
            CALL Printchar

            CALL Limpabarra
            CALL Printbarra

            fim_if_colisao_chao: NOP

        ; Imprime na tela a nova direção da bola *****************************

            MOV R1, M[posicao_atual_X_bola]
            MOV M[argumento_pos_coluna_Printchar], R1
            MOV R2, M[posicao_atual_Y_bola]
            MOV M[argumento_pos_linha_Printchar], R2
            MOV R1, bola
            MOV R1, M[R1]
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            MOV R2, M[posicao_anterior_Y_bola]
            MOV M[argumento_pos_linha_Printchar], R2
            MOV R1, M[posicao_anterior_X_bola]
            MOV M[argumento_pos_coluna_Printchar], R1
            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            CALL SetTimer

            POP R2
            POP R1
            RTI 
            
;------------------------------------------------------------------------------
; StartGame - Começa o jogo
;------------------------------------------------------------------------------
StartGame:  CALL SetTimer
            RTI

;------------------------------------------------------------------------------
; Função Main
;------------------------------------------------------------------------------
Main:			ENI

				MOV		R1, INITIAL_SP
				MOV		SP, R1		 		; We need to initialize the stack
				MOV		R1, CURSOR_INIT		; We need to initialize the cursor 
				MOV		M[ CURSOR ], R1		; with value CURSOR_INIT
                
          ; Printa o menu ---------------------------------

                CALL Printmenu
                            
          ; Printa a bola ---------------------------------
                
                MOV R1, COORDENADA_INICIAL_Y_BOLA
                MOV M[argumento_pos_linha_Printchar], R1 
                MOV R1, COORDENADA_INICIAL_X_BOLA
                MOV M[argumento_pos_coluna_Printchar], R1      
                MOV R1, bola   
                MOV R1, M[R1] 
                MOV M[argumento_char_Printchar], R1   
                CALL Printchar

          ; Printa a barra --------------------------------

                CALL Printbarra

Cycle: 			BR		Cycle	
Halt:           BR		Halt