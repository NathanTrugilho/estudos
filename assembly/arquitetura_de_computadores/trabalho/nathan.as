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

TAMANHO_BARRA               EQU     12d
POSICAO_LINHA_BARRA         EQU     22d
COLUNA_COMECO_BARRA         EQU     34d
COORDENADA_INICIAL_X_BOLA   EQU     21d
COORDENADA_INICIAL_Y_BOLA   EQU     40d
TEMPO_DE_ATUALIZACAO        EQU     5d

;------------------------------------------------------------------------------
; ZONA II: definicao de variaveis
;          Pseudo-instrucoes : WORD - palavra (16 bits)
;                              STR  - sequencia de caracteres (cada ocupa 1 palavra: 16 bits).
;          Cada caracter ocupa 1 palavra
;------------------------------------------------------------------------------

                ORIG    8000h

argumento_pos_linha_Printbarra     WORD    0d
argumento_pos_coluna_Printbarra    WORD    0d

argumento_string_Printmenu         WORD    0d

argumento_pos_linha_Printchar      WORD    0d
argumento_pos_coluna_Printchar     WORD    0d
argumento_char_Printchar           WORD    0d

proxima_posicao_X_bola             WORD    21d ;COORDENADA_INICIAL_X_BOLA
proxima_posicao_Y_bola             WORD    40d ;COORDENADA_INICIAL_Y_BOLA

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

            DEC M[posicao_fim_barra]
            MOV R1, M[posicao_fim_barra]
            MOV M[argumento_pos_coluna_Printchar], R1

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
            CMP R1, 79
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

            MOV R1, M[proxima_posicao_X_bola]
            DEC R1
            MOV M[proxima_posicao_X_bola], R1

            MOV M[argumento_pos_linha_Printchar], R1 

            MOV R1, M[proxima_posicao_Y_bola]
            INC R1
            MOV M[proxima_posicao_Y_bola], R1

            MOV M[argumento_pos_coluna_Printchar], R1      
            MOV R1, bola   
            MOV R1, M[R1] 
            MOV M[argumento_char_Printchar], R1   
            CALL Printchar

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

                MOV R1, COORDENADA_INICIAL_X_BOLA
                MOV M[argumento_pos_linha_Printchar], R1 
                MOV R1, COORDENADA_INICIAL_Y_BOLA
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