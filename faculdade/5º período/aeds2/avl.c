#include <stdio.h>
#include <stdlib.h>

// Definição da estrutura do nó da árvore
typedef struct Node {
    int key;
    struct Node *left;
    struct Node *right;
    int height;
} Node;

// Função para criar um novo nó
Node* newNode(int key) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    node->height = 1;
    return node;
}

// Função para obter a altura de um nó
int height(Node* node) {
    if (node == NULL) return 0;
    return node->height;
}

// Função para obter o máximo de dois inteiros
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Função para rodar a árvore para a direita
Node* rightRotate(Node* y) {
    Node* x = y->left;
    Node* T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = max(height(y->left), height(y->right)) + 1;
    x->height = max(height(x->left), height(x->right)) + 1;

    return x;
}

// Função para rodar a árvore para a esquerda
Node* leftRotate(Node* x) {
    Node* y = x->right;
    Node* T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;

    return y;
}

// Função para obter o fator de balanceamento de um nó
int getBalance(Node* node) {
    if (node == NULL) return 0;
    return height(node->left) - height(node->right);
}

// Função para inserir um nó na árvore AVL
Node* insert(Node* node, int key) {
    if (node == NULL) return newNode(key);

    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);
    else // Chaves iguais não são permitidas na árvore AVL
        return node;

    // Atualiza a altura do nó atual
    node->height = 1 + max(height(node->left), height(node->right));

    // Obtem o fator de balanceamento do nó
    int balance = getBalance(node);

    // Caso o nó fique desbalanceado, existem 4 casos de rotação
    // Caso esquerda-esquerda
    if (balance > 1 && key < node->left->key)
        return rightRotate(node);
    
    // Caso esquerda-direita
    if (balance > 1 && key > node->left->key) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // Caso direita-direita
    if (balance < -1 && key > node->right->key)
        return leftRotate(node);

    // Caso direita-esquerda
    if (balance < -1 && key < node->right->key) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    // Retorna o ponteiro do nó (inalterado)
    return node;
}

// Função para percorrer a árvore AVL em ordem
void inOrder(Node* root) {
    if (root != NULL) {
        inOrder(root->left);
        printf("%d ", root->key);
        inOrder(root->right);
    }
}

// Função principal
int main() {
    Node* root = NULL;

    // Inserindo elementos na árvore AVL
    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 30);
    root = insert(root, 40);
    root = insert(root, 50);
    root = insert(root, 25);

    // Imprimindo a árvore AVL em ordem
    printf("Arvore avl em ordem: ");
    inOrder(root);
    printf("\n");

    return 0;
}
