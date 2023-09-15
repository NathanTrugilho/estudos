#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 10

typedef struct Node {
    int key;
    int data;
    struct Node* next;
} Node;

Node* hashTable[TABLE_SIZE];

void initHashTable() {
    int i;
    for (i = 0; i < TABLE_SIZE; i++)
        hashTable[i] = NULL;
}

void insert(int key, int data) {
    int index = key % TABLE_SIZE;

    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->key = key;
    newNode->data = data;
    newNode->next = NULL;

    if (hashTable[index] == NULL) {
        hashTable[index] = newNode;
    } else {
        Node* current = hashTable[index];
        while (current->next != NULL)
            current = current->next;
        current->next = newNode;
    }
}

Node* search(int key) {
    int index = key % TABLE_SIZE;

    if (hashTable[index] == NULL)
        return NULL;

    Node* current = hashTable[index];
    while (current != NULL) {
        if (current->key == key)
            return current;
        current = current->next;
    }
    return NULL;
}

void display() {
    int i;
    for (i = 0; i < TABLE_SIZE; i++) {
        printf("Index %d: ", i);
        Node* current = hashTable[i];
        while (current != NULL) {
            printf("(%d, %d) ", current->key, current->data);
            current = current->next;
        }
        printf("\n");
    }
}

int main() {
    initHashTable();

    insert(10, 100);
    insert(22, 200);
    insert(33, 300);
    insert(55, 400);
    insert(25, 500);

    display();

    Node* result = search(33);
    if (result != NULL)
        printf("Element found: (%d, %d)\n", result->key, result->data);
    else
        printf("Element not found.\n");

    return 0;
}
