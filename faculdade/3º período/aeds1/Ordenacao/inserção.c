#include <stdio.h>

void insertion_sort(int arr[], int n) {
    int i, j, key;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        /* Move os elementos do array que são maiores que a chave
           para uma posição à frente de sua posição atual */
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[] = {5, 3, 8, 4, 2};
    int n = sizeof(arr) / sizeof(arr[0]);
    int i;

    printf("Array antes da ordenação:\n");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    insertion_sort(arr, n);

    printf("\nArray depois da ordenação:\n");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
