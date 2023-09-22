;-------------------------------------------------------------------------------
; ZONA LIXEIRA: partes de códigos que não sei se vou usar em algum momento, mas
; vou salvá-los aqui caso necessário no futuro 
;-------------------------------------------------------------------------------
;
;-------------------------------------------------------------------------------
; Função Timer - Função que inicia o jogo                    
;-------------------------------------------------------------------------------
;Timer:      PUSH R1
;            PUSH R2
;
;            MOV R1, 12d
;            MOV R2, 40d
;            SHL R1, 8d
;            OR R1, R2
;
;            MOV M[ CURSOR ], R1
;            MOV R2, M[ bola ]
;            MOV M[ IO_WRITE ], R2
;            INC M[ bola ]
;
;            CALL SetTimer
;
;           POP R2
;           POP R1
;           RTI 

; Verifica se a bola colidiu com as paredes laterais, o teto ou o chão

;            MOV R1, M[posicao_atual_X_bola]
;            ADD R1, M[movimentacao_X_bola]
;            CMP R1, 0
;            JMP.NZ fim_if_colisao_parede_esquerda
;            MOV R1, 1
;            MOV M[movimentacao_X_bola], R1
;            fim_if_colisao_parede_esquerda: NOP
;
;            MOV M[argumento_pos_linha_Printchar], R2
;            MOV M[argumento_pos_coluna_Printchar], R1
;            MOV R1, bola
;            MOV R1, M[R1]
;            MOV M[argumento_char_Printchar], R1
;            CALL Printchar
;
;            MOV R1, M[posicao_anterior_X_bola]
;            MOV M[argumento_pos_coluna_Printchar], R1
;            MOV R2, M[posicao_anterior_Y_bola]
;            MOV M[argumento_pos_linha_Printchar], R2
;            MOV R1, ' '
;            MOV M[argumento_char_Printchar], R1
;            CALL Printchar
;           
;********************************************************************************
;------------------------------------------------------------------------------
; ZONA 0: compilar e rodar programa
; Linux:        ./p3as-linux nathan.as; java -jar p3sim.jar nathan.exe
; Windows:      .\p3as-win.exe .\nathan.as ; java -jar .\p3sim.jar .\nathan.exe
;------------------------------------------------------------------------------
; ZONA I: Definicao de constantes
;         Pseudo-instrucao : EQU
;------------------------------------------------------------------------------
; Constantes do Sistema
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

TAMANHO_BARRA               EQU     12d ;Deve ser um múltiplo de 3
POSICAO_LINHA_BARRA         EQU     22d
COLUNA_COMECO_BARRA         EQU     34d
COORDENADA_INICIAL_X_BOLA   EQU     30d
COORDENADA_INICIAL_Y_BOLA   EQU     17d
TEMPO_DE_ATUALIZACAO        EQU     10d

;------------------------------------------------------------------------------
; ZONA II: definicao de variaveis
;          Pseudo-instrucoes : WORD - palavra (16 bits)
;                              STR  - sequencia de caracteres (cada ocupa 1 palavra: 16 bits).
;          Cada caracter ocupa 1 palavra
;------------------------------------------------------------------------------

                ORIG    8000h
tamanho_pedaco_barra               WORD    0d

argumento_pos_linha_Printbarra     WORD    0d
argumento_pos_coluna_Printbarra    WORD    0d

argumento_string_Printmenu         WORD    0d

argumento_pos_linha_Printchar      WORD    0d
argumento_pos_coluna_Printchar     WORD    0d
argumento_char_Printchar           WORD    0d

movimentacao_X_bola                WORD    0d
movimentacao_Y_bola                WORD    1d
posicao_anterior_X_bola            WORD    0d
posicao_anterior_Y_bola            WORD    0d
posicao_atual_X_bola               WORD    COORDENADA_INICIAL_X_BOLA
posicao_atual_Y_bola               WORD    COORDENADA_INICIAL_Y_BOLA 
    
posicao_inicio_barra               WORD    0d
posicao_fim_barra                  WORD    0d

Line1           STR     '+==================+===========================================+===============+'
Line2           STR     '| Bolas: O - O - O |               Nathan                      | Pontos: 00000 |'
Line3           STR     '+==================+===========================================+===============+'
Line4           STR     '|                                                                              |'
Line5           STR     '|                                                                              |'
Line6           STR     '|       ################################################################       |'
Line7           STR     '|       ################################################################       |'
Line8           STR     '|       ################################################################       |'
Line9           STR     '|       ################################################################       |'
Line10          STR     '|       ################################################################       |'
Line11          STR     '|       ################################################################       |'
Line12          STR     '|       ################################################################       |'
Line13          STR     '|       ################################################################       |'  
Line14          STR     '|       ################################################################       |'
Line15          STR     '|       ################################################################       |'
Line16          STR     '|       ################################################################       |'
Line17          STR     '|       ################################################################       |'
Line18          STR     '|                                                                              |'
Line19          STR     '|                                                                              |'
Line20          STR     '|                                                                              |'
Line21          STR     '|                                                                              |'
Line22          STR     '|                                                                              |'
Line23          STR     '|                                                                              |'
Line24          STR     '\______________________________________________________________________________/', FIM_TEXTO

bola            WORD     'O'   
;------------------------------------------------------------------------------
; ZONA III: definicao de tabela de interrupções
;------------------------------------------------------------------------------
                ORIG    FE00h
INT0            WORD    movimenta_barra_esquerda
INT1            WORD    movimenta_barra_direita

                ORIG    FE0Fh
INT15           WORD    Timer

;------------------------------------------------------------------------------
; ZONA IV: codigo
;        conjunto de instrucoes Assembly, ordenadas de forma a realizar
;        as funcoes pretendidas
;------------------------------------------------------------------------------
                ORIG    0000h
                JMP     Main
;------------------------------------------------------------------------------
; Função esqueleto
;------------------------------------------------------------------------------

Esqueleto:  PUSH R1
            PUSH R2
            PUSH R3

            POP R3
            POP R2
            POP R1
            RET
;-----------------------------------------------------------------------------------------
; Função movimenta_barra_esquerda - O nome é bem óbvio, não preciso explicar
;                                  Usar o caractere 'a' em IVAD0 no simulador
;-----------------------------------------------------------------------------------------

movimenta_barra_esquerda:  PUSH R1
            PUSH R2
            
            MOV R1, M[posicao_inicio_barra]
            CMP R1, 1
            JMP.Z final_if_movimenta_barra_esquerda

            MOV R1, POSICAO_LINHA_BARRA
            MOV M[argumento_pos_linha_Printchar], R1

            MOV R1, M[posicao_fim_barra]
            MOV M[argumento_pos_coluna_Printchar], R1
            DEC M[posicao_fim_barra]

            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            DEC M[posicao_inicio_barra]
            MOV R1, M[posicao_inicio_barra]
            MOV M[argumento_pos_coluna_Printchar], R1

            MOV R1, '='
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            final_if_movimenta_barra_esquerda: NOP
            POP R2
            POP R1
            RTI

;-----------------------------------------------------------------------------------------
; Função movimenta_barra_direita - O nome é bem óbvio, não preciso explicar
;                                  Usar o caractere 'd' em IVAD1 no simulador
;-----------------------------------------------------------------------------------------

movimenta_barra_direita:  PUSH R1
            PUSH R2
            
            MOV R1, M[posicao_fim_barra]
            CMP R1, 78
            JMP.Z final_if_movimenta_barra_direita

            MOV R1, POSICAO_LINHA_BARRA
            MOV M[argumento_pos_linha_Printchar], R1

            MOV R1, M[posicao_inicio_barra]
            INC M[posicao_inicio_barra]
            MOV M[argumento_pos_coluna_Printchar], R1

            MOV R1, ' '
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            MOV R1, M[posicao_fim_barra]
            INC M[posicao_fim_barra]
            MOV M[argumento_pos_coluna_Printchar], R1
            INC M[argumento_pos_coluna_Printchar]

            MOV R1, '='
            MOV M[argumento_char_Printchar], R1
            CALL Printchar

            final_if_movimenta_barra_direita: NOP
            POP R2
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
; Função Printbarra - Imprime a barra com a posição especificada pelas 
; constantes "POSICAO_LINHA_BARRA", "COLUNA_COMECO_BARRA" com o tamanho definido 
; em "TAMANHO_BARRA"
;
; Recebe como parâmetros: a posição da linha guardada em "argumento_pos_linha_Printbarra"
;                         a posição da coluna guardada em "argumento_pos_coluna_Printbarra"
;-----------------------------------------------------------------------------------------

Printbarra: PUSH R1
            PUSH R2
            PUSH R3

        ;Define a posição do inicio e fim da barra

            MOV R1, COLUNA_COMECO_BARRA
            MOV M[posicao_inicio_barra], R1
            ADD R1, TAMANHO_BARRA
            DEC R1
            MOV M[posicao_fim_barra], R1         
        ;______________________________________________

            MOV R3, POSICAO_LINHA_BARRA
            SHL R3, 8d
            MOV R2, COLUNA_COMECO_BARRA
            OR R3, R2
            MOV R2, TAMANHO_BARRA
            MOV R1, '='

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
            MOV M[tamanho_pedaco_barra], R1

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
            MOV R4, R0

            loop_Printmenu: CMP R1, R2
            JMP.Z fim_loop_Printmenu
            CMP R4, 80

            JMP.NZ LOOP_NEXT_LINE       ; SE FOR ZERO, DEVE PASSAR PARA A PRÓXIMA LINHA
            SUB R3, R4
            MOV R4, 1
            SHL R4, 8
            ADD R3, R4
            MOV R4, R0

            LOOP_NEXT_LINE: MOV M[CURSOR], R3
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
            
; Faz o processo de movimento da bola com base nas "direções" que ela vai seguir. Os argumentos de direção estão guardados em "movimentacao_X_bola" e "movimentacao_Y_bola"

            MOV R1, M[posicao_atual_X_bola]
            MOV M[posicao_anterior_X_bola], R1
            ADD R1, M[movimentacao_X_bola]
            MOV M[posicao_atual_X_bola], R1

            MOV R2, M[posicao_atual_Y_bola]
            MOV M[posicao_anterior_Y_bola], R2
            ADD R2, M[movimentacao_Y_bola]
            MOV M[posicao_atual_Y_bola], R2

; Verifica se a bola bateu na barra e faz o cálculo de sua nova direção caso verdade 

            MOV R1, M[posicao_atual_Y_bola]
            CMP R1, POSICAO_LINHA_BARRA
            JMP.NZ fim_if_colisao_barra
            
            MOV R2, M[posicao_atual_X_bola]
            CMP R2, M[posicao_inicio_barra]
            JMP.N fim_if_colisao_barra
            MOV R1, M[posicao_fim_barra]

            CMP R2, R1
            JMP.P fim_if_colisao_barra

        ;Faz o cálculo da nova direção da bola após a colisão *****

            ; Lado esquerdo da barra ------------------------------

            MOV R1, M[posicao_atual_X_bola]
            ADD R1, M[movimentacao_X_bola]
            MOV R2, M[posicao_inicio_barra]
            ADD R2, M[tamanho_pedaco_barra]

            CMP R1, R2
            JMP.P fim_if_colisao_esquerda_barra
            MOV R1, M[movimentacao_X_bola]
            DEC R1
            CMP R1, -2
            JMP.NZ fim_if_correcao_esquerda_barra
            INC R1
            fim_if_correcao_esquerda_barra: NOP
            MOV M[movimentacao_X_bola], R1
            fim_if_colisao_esquerda_barra: NOP

            ; Lado direito da barra ------------------------------

            MOV R1, M[posicao_atual_X_bola]
            ADD R1, M[movimentacao_X_bola]
            MOV R2, M[posicao_fim_barra]
            DEC R2
            SUB R2, M[tamanho_pedaco_barra]

            CMP R1, R2
            JMP.N fim_if_colisao_direita_barra
            MOV R1, M[movimentacao_X_bola]
            INC R1
            CMP R1, 2
            JMP.NZ fim_if_correcao_direita_barra
            DEC R1
            fim_if_correcao_direita_barra: NOP
            MOV M[movimentacao_X_bola], R1
            fim_if_colisao_direita_barra: NOP

            ; Caso geral (bater no meio da barra)-----------------

            MOV R1, -1
            MOV M[movimentacao_Y_bola], R1

        ;Caso não haja colisões, o código vem para cá *************
        
            fim_if_colisao_barra: NOP
            CALL SetTimer

            POP R2
            POP R1
            RTI 

;------------------------------------------------------------------------------
; Função Main
;------------------------------------------------------------------------------
Main:			ENI

				MOV		R1, INITIAL_SP
				MOV		SP, R1		 		; We need to initialize the stack
				MOV		R1, CURSOR_INIT		; We need to initialize the cursor 
				MOV		M[ CURSOR ], R1		; with value CURSOR_INIT
                
;           Printa o menu ********************************

                CALL Printmenu
                            
;           Printa a bola ********************************
                
                MOV R1, COORDENADA_INICIAL_Y_BOLA
                MOV M[argumento_pos_linha_Printchar], R1 
                MOV R1, COORDENADA_INICIAL_X_BOLA
                MOV M[argumento_pos_coluna_Printchar], R1      
                MOV R1, bola   
                MOV R1, M[R1] 
                MOV M[argumento_char_Printchar], R1   
                CALL Printchar

;           Printa a barra *******************************

                CALL Printbarra

;           Comeca o jogo ********************************

                CALL SetTimer           

Cycle: 			BR		Cycle	
Halt:           BR		Halt