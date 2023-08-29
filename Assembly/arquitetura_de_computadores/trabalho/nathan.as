;------------------------------------------------------------------------------
; ZONA 0: compilar e rodar programa
; Fedora:       ./p3as-linux nathan.as; java -jar p3sim.jar nathan.exe
; Windows:      .\p3as-win.exe .\nathan.as ; java -jar .\p3sim.jar .\nathan.exe
;------------------------------------------------------------------------------
; ZONA I: Definicao de constantes
;         Pseudo-instrucao : EQU
;------------------------------------------------------------------------------
CR              EQU     0Ah
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
; ZONA II: definicao de variaveis
;          Pseudo-instrucoes : WORD - palavra (16 bits)
;                              STR  - sequencia de caracteres (cada ocupa 1 palavra: 16 bits).
;          Cada caracter ocupa 1 palavra
;------------------------------------------------------------------------------

                ORIG    8000h

LinePrintstr    WORD    0d
StringPrintstr  WORD    0d
Line1           STR     '+---------------+---------------------+----------------------------------------+', FIM_TEXTO
Line2           STR     '| Pontos: 00000 |  Vidas restantes: 3 |                                        |', FIM_TEXTO
Line3           STR     '+---------------+---------------------+----------------------------------------+', FIM_TEXTO


;------------------------------------------------------------------------------
; ZONA II: definicao de tabela de interrupções
;------------------------------------------------------------------------------
                ORIG    FE00h
;INT0            WORD    WriteCharacter

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

;------------------------------------------------------------------------------
; Função Printstr
;------------------------------------------------------------------------------

Printstr:   PUSH R1
            PUSH R2
            PUSH R3
            PUSH R4

            MOV R4, M[StringPrintstr] 
            MOV R1, M[R4]
            MOV R2, FIM_TEXTO
            MOV R3, M[LinePrintstr] ; POSIÇÃO DE PRINT  
            SHL R3, 8

            VOLTA_LOOP: CMP R1, R2
            JMP.Z FIM_LOOP
            MOV M[CURSOR], R3
            MOV M[IO_WRITE], R1
            INC R3
            INC R4
            MOV R1, M[R4]
            JMP VOLTA_LOOP
            FIM_LOOP: NOP
            
            POP R4
            POP R3
            POP R2
            POP R1
            RET

;------------------------------------------------------------------------------
; Função Main
;------------------------------------------------------------------------------
Main:			ENI

				MOV		R1, INITIAL_SP
				MOV		SP, R1		 		; We need to initialize the stack
				MOV		R1, CURSOR_INIT		; We need to initialize the cursor 
				MOV		M[ CURSOR ], R1		; with value CURSOR_INIT

                MOV R1, R0
                MOV M[LinePrintstr], R1     ; LinePrintstr tem o endereço 8k. Guarda o valor de R1 (0) no endereço 8k
                MOV R1, Line1               ; Por ser um vetor, guarda o endereço de line1(8002) em R1
                MOV M[StringPrintstr], R1   ; Guarda no endereço de StringPrintstr (8001) o valor de R1 (8002)
                CALL Printstr

                MOV R1, 1
                MOV M[LinePrintstr], R1     
                MOV R1, Line2               
                MOV M[StringPrintstr], R1   
                CALL Printstr

                MOV R1, 2
                MOV M[LinePrintstr], R1     
                MOV R1, Line3               
                MOV M[StringPrintstr], R1   
                CALL Printstr
                
Cycle: 			BR		Cycle	
Halt:           BR		Halt