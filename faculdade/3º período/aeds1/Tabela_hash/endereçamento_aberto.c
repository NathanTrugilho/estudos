#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 10
#define DELETED -1

int hashTable[TABLE_SIZE];

void initHashTable() {
    int i;
    for (i = 0; i < TABLE_SIZE; i++)
        hashTable[i] = -1;
}

int hashFunction(int key) {
    return key % TABLE_SIZE;
}

void insert(int key) {
    int index = hashFunction(key);

    while (hashTable[index] != -1 && hashTable[index] != DELETED) {
        index = (index + 1) % TABLE_SIZE;
    }

    hashTable[index] = key;
}

int search(int key) {
    int index = hashFunction(key);

    while (hashTable[index] != -1) {
        if (hashTable[index] == key)
            return index;
        index = (index + 1) % TABLE_SIZE;
    }

    return -1;
}

void removeKey(int key) {
    int index = search(key);
    if (index != -1)
        hashTable[index] = DELETED;
}

void display() {
    int i;
    for (i = 0; i < TABLE_SIZE; i++) {
        printf("Index %d: ", i);
        if (hashTable[i] == -1)
            printf("Empty");
        else if (hashTable[i] == DELETED)
            printf("Deleted");
        else
            printf("%d", hashTable[i]);
        printf("\n");
    }
}

int main() {
    initHashTable();

    insert(10);
    insert(22);
    insert(33);
    insert(55);
    insert(25);

    display();

    int result = search(33);
    if (result != -1)
        printf("Element found at index %d\n", result);
    else
        printf("Element not found.\n");

    removeKey(33);
    display();

    return 0;
}
