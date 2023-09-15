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
Text			STR     'Nathan Trugilho Braga', FIM_TEXTO
RowIndex		WORD	0d
ColumnIndex		WORD	0d
TextIndex		WORD	0d


;------------------------------------------------------------------------------
; ZONA II: definicao de tabela de interrupções
;------------------------------------------------------------------------------
                ORIG    FE00h
INT0            WORD    WriteCharacter

;------------------------------------------------------------------------------
; ZONA IV: codigo
;        conjunto de instrucoes Assembly, ordenadas de forma a realizar
;        as funcoes pretendidas
;------------------------------------------------------------------------------
                ORIG    0000h
                JMP     Main

;------------------------------------------------------------------------------
; Rotina de Interrupção WriteCharacter
;------------------------------------------------------------------------------
WriteCharacter: PUSH	R1
				PUSH	R2

				MOV		R1, M[ TextIndex ]
				MOV		R1, M[ R1 ]
				CMP 	R1, FIM_TEXTO
				JMP.Z	Halt
				MOV     M[ IO_WRITE ], R1
				INC		M[ RowIndex ]
				INC		M[ ColumnIndex ]
				INC		M[ TextIndex ]
				MOV		R1, M[ RowIndex ]
				MOV		R2, M[ ColumnIndex ]
				SHL		R1, ROW_SHIFT
				OR		R1, R2
				MOV		M[ CURSOR ], R1

				POP		R2
				POP		R1
				RTI

;------------------------------------------------------------------------------
; Função Main
;------------------------------------------------------------------------------
Main:			ENI

				MOV		R1, INITIAL_SP
				MOV		SP, R1		 		; We need to initialize the stack
				MOV		R1, CURSOR_INIT		; We need to initialize the cursor 
				MOV		M[ CURSOR ], R1		; with value CURSOR_INIT
				MOV     R1, Text
				MOV		M[ TextIndex ], R1

				MOV R1, m[Text]
				MOV R2, FIM_TEXTO
				MOV R3, 50
				MOV R4, 11
				SHL R4, 8
				OR R3, R4
				MOV R5, 1
				FAZDENOVO: CMP R1, R2
				JMP.Z FAZALGO
				MOV M[CURSOR], R3
				MOV M[IO_WRITE], R1
				MOV R1, M[R5 + Text]
				INC R3
				INC R5
				JMP FAZDENOVO
				FAZALGO: NOP


Cycle: 			BR		Cycle	
Halt:           BR		Halt