#include <stdio.h>

void desce_heap(int arr[], int n, int i) {
    //define a posicao do pai
    int maior = i;
    //define a posicao do filho da esquerda
    int esq = 2 * i + 1;
    //define a posicao do filho da direita
    int dir = 2 * i + 2;

    //verifica se o filho da esquerda existe (se a posicao dele e menor que o tamanho maximo do vetor) e se ele e maior que o pai
    if (esq < n && arr[esq] > arr[maior])
        maior = esq;
    //faz o mesmo para o filho da direita
    if (dir < n && arr[dir] > arr[maior])
        maior = dir;

    //faz a troca entre o filho maior que o pai. Caso a variavel "maior" seja igual a "i", nao houve uma troca, ou seja, a funcao deve acabar
    if (maior != i) {
        int temp = arr[i];
        arr[i] = arr[maior];
        arr[maior] = temp;
        //chama a funcao novamente para verificar se o elemento pode descer novamente
        desce_heap(arr, n, maior);
    }
}

//funcao para verificar se o filho e menor que o pai. Deve ser chamada quando um elemento e inserido num heap de maximo.
void sobe_heap(int arr[], int i) {
    int pai = (i - 1) / 2;
    if (arr[pai] < arr[i]) {
        int temp = arr[i];
        arr[i] = arr[pai];
        arr[pai] = temp;
        sobe_heap(arr, pai);
    }
}

//faz um loop comecando um subnivel acima dos ultimos filhos (filhos mais abaixo) e chama a funcao desce_heap para formar um heap de maximo
void constroi_heap_max(int arr[], int n) {
    /*for (int i = n / 2 - 1; i >= 0; i--) {
        desce_heap(arr, n, i);
    }*/
    for (int i = 1; i < n; i++){
        sobe_heap(arr, i);
    }
}


//funcao principal
void heapsort(int arr[], int n) {
    //monta o heap de maximo
    constroi_heap_max(arr, n);

    //Ordena o vetor. O laco comeca trocando o pai raiz com o ultimo elemento do vetor e usa o "desce_heap" no elemento que foi trocado
    for (int i = n - 1; i >= 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;

        desce_heap(arr, i, 0);
    }
}

int main() {
    int vetor[] = {12, 11, 13, 5, 6, 7, 1, 3, 0};
    int tamanho = sizeof(vetor)/sizeof(vetor[0]);

    heapsort(vetor, tamanho);

    printf("Array ordenado: \n");
    for (int i=0; i < tamanho; i++) {
        printf("%d ", vetor[i]);
    }
    return 0;
}
