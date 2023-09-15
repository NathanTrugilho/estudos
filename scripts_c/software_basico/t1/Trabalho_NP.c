//Feito por Nathan Trugilho e Pedro Tesch.

#include <stdio.h>
#include <stdlib.h>

//Defining instructions 
#define byte unsigned char
#define load_mem 0
#define load_val 1
#define store    2
#define add      3
#define sub      4
#define mul      5
#define div      6
#define inc      7
#define dec      8
#define and      9
#define or       10
#define not      11
#define jmp      12
#define jz       13
#define jnz      14
#define jg       15
#define jl       16
#define jge      17
#define jle      18
#define hlt      19

//Defining flags
#define zeroacc  1
#define carry    2
#define overflow 4


typedef struct __inst{
    byte opcode;
    byte operand;
}inst;

//Funcion that updates the status
void update_stat(byte *stat, byte acc, int tipo){
    
	*stat = 0;

	if(!acc){
        *stat = 1;
    	return;
    }

    *stat = *stat | tipo;
}

//Main function
int main(int argc, char * argv[]){
    inst program[256];
    FILE *binary_file;

    //Registers
    short acc = 0; 
	byte pc = 0;   
	byte stat = 0; 

    //Defining pointer to archive 
    binary_file = fopen(argv[1], "rb");

	//Error message if opening goes wrong
    if(binary_file == NULL){
        printf("->Erro ao abrir o arquivo!: %s\n", argv[1]);
        exit(0);
    }

    byte instruction[2];

	//Opening and reading the file
    while(fread(instruction, sizeof(byte), 2, binary_file)){
        program[pc].opcode = instruction[0];
        program[pc].operand = instruction[1];
        pc++;
    }
    fclose(binary_file);

    //starting instructions
    pc = 0;
    short memory[256];
    byte opcode = 0;
    byte operand;

	//Main loop
    while(opcode != hlt){

        opcode = program[pc].opcode;
        operand = program[pc].operand;
	
        switch(opcode){

        case load_mem:
            acc = memory[operand];
            update_stat(&stat, acc, zeroacc);
            pc++;
        break;

		case load_val:
			acc = operand;
            update_stat(&stat, acc, zeroacc);
			pc++;
			break;

		case store:
			memory[operand] = acc;
			pc++;
			break;

		case add:
			// checks for carry
			if ((short)(acc + memory[operand]) > 127 || (short)(acc + memory[operand]) < -128){
			    update_stat(&stat, acc, carry);
			}
			else{
                update_stat(&stat, acc, 0);
			}
			acc += memory[operand];
			pc++;
			break;

		case sub:
			// checks for carry
			if ((short)(acc + memory[operand]) > 127 || (short)(acc + memory[operand]) < -128){
			    update_stat(&stat, acc, carry);
			}
			else{
                update_stat(&stat, acc, 0);
			}
			acc -= memory[operand];
			pc++;
			break;

		case mul:
			// checks for overflow
			if ((short)(acc * memory[operand]) > 127 || (short)(acc * memory[operand]) < -128){
			    update_stat(&stat, acc, overflow);
			}
			else{
                update_stat(&stat, acc, 0);
			}
			acc *= memory[operand];
			pc++;
			break;

		case div:
			acc /= memory[operand];
			update_stat(&stat, acc, 0);
			pc++;
			break;

		case inc:
			// checks for carry
			if ((short)(acc + 1 > 127 || (short)(acc + 1) < -128)){
			    update_stat(&stat, acc, carry);
			}
			else{
                update_stat(&stat, acc, 0);
			}
			++acc;
			pc++;
			break;

		case dec:
			// checks for carry
			if ((short)(acc - 1 > 127 || (short)(acc - 1) < -128)){
			    update_stat(&stat, acc, carry);
			}
			else{
                update_stat(&stat, acc, 0);
			}
			--acc;
			pc++;
			break;

		case and:
			acc &= memory[operand];
			update_stat(&stat, acc, 0);
			pc++;
			break;

		case or:
			acc |= memory[operand];
			update_stat(&stat, acc, 0);
			pc++;
			break;

		case not:
			acc = ~acc;
			update_stat(&stat, acc, 0);
			pc++;
			break;

		case jmp:
			pc = operand/2;
			break;

		case jz:
			if (acc = 0)
				pc = operand/2;
			else
				pc += 1;
			break;

		case jnz:
			if (acc != 0)
				pc = operand/2;
			else
				pc += 1;
			break;

		case jg:
			if (acc > 0)
				pc = operand/2;
			else
				pc += 1;
			break;

		case jl:
			if (acc < 0)
				pc = operand/2;
			else
				pc += 1;
			break;

		case jge:
			if (acc >= 0)
				pc = operand/2;
			else
				pc += 1;
			break;

		case jle:
			if (acc <= 0)
				pc = operand/2;
			else
				pc += 1;
			break;

		case hlt:
			printf("ACC: %d\nSTAT: %.2X\n", acc, stat);
            break;
        }
    }
    return 0;
}