#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>

#define FILENAME "buffer.txt"
#define LOCKFILE "buffer.txt.lock"

void write_value_to_file(int value) {
    FILE *file = fopen(FILENAME, "a");
    if (file == NULL) {
        perror("Erro ao abrir o arquivo");
        exit(1);
    }
    fprintf(file, "%d\n", value);
    fclose(file);
}

int read_value_from_file() {
    FILE *file = fopen(FILENAME, "r");
    if (file == NULL) {
        perror("Erro ao abrir o arquivo");
        exit(1);
    }
    int value;
    fscanf(file, "%d", &value);
    fclose(file);
    return value;
}

void create_lock_file() {
    HANDLE lockfile = CreateFile(LOCKFILE, GENERIC_WRITE, 0, NULL, CREATE_NEW, FILE_ATTRIBUTE_NORMAL, NULL);
    if (lockfile == INVALID_HANDLE_VALUE) {
        perror("Erro ao criar o arquivo de bloqueio");
        exit(1);
    }
    CloseHandle(lockfile);
}

void remove_lock_file() {
    if (!DeleteFile(LOCKFILE)) {
        perror("Erro ao remover o arquivo de bloqueio");
        exit(1);
    }
}

int main() {
    srand(time(NULL));

    // Inicializar o arquivo com 10 inteiros
    FILE *file = fopen(FILENAME, "w");
    if (file == NULL) {
        perror("Erro ao criar o arquivo");
        return 1;
    }
    for (int i = 0; i < 10; i++) {
        fprintf(file, "%d\n", i);
    }
    fclose(file);

    HANDLE hMutex = CreateMutex(NULL, FALSE, NULL);
    if (hMutex == NULL) {
        perror("Erro ao criar o mutex");
        return 1;
    }

    HANDLE hChildProcess;

    // Criação do processo filho
    STARTUPINFO si;
    PROCESS_INFORMATION pi;

    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));

    char commandLine[256] = "consumidor.exe";
    if (!CreateProcess(NULL, commandLine, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi)) {
        perror("Erro ao criar o processo consumidor");
        return 1;
    }

    hChildProcess = pi.hProcess;

    while (1) {
        Sleep(1000 + rand() % 3000);  // Tempo de espera aleatório (1 a 3 segundos)

        // Verificar se o arquivo de bloqueio existe
        while (GetFileAttributes(LOCKFILE) != INVALID_FILE_ATTRIBUTES) {
            Sleep(1000);
        }

        create_lock_file();
        int value = rand() % 100;
        write_value_to_file(value);
        printf("[Produtor] %d\n", value);
        remove_lock_file();
    }

    CloseHandle(hChildProcess);
    CloseHandle(hMutex);

    return 0;
}
