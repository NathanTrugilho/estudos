#include <stdio.h>
#include <stdlib.h>

typedef struct __node {
    char color;
    int key;
    struct __node* left;
    struct __node* right;
    struct __node* father;
} node ;



void RR(node * no){

    node * aux;
    aux = no->left;
    aux->right->father = no;
    no->left = aux->right;
    aux->right = no;
    aux->father = no->father;
    no -> father = aux;
    no = aux;
}

void LL(node * no){
    node * aux;
    aux = no->right;
    aux->left->father = no;
    no->right = aux->left;
    aux->left = no;
    aux->father = no->father;
    no -> father = aux;
    no = aux;
}

void fixup_insertion(node * root, node * inserted){
    if(inserted->father->color == 'B'){
        return;
    }

    node * u; 
    while(inserted->father != NULL && inserted->father->color == 'R'){
        if(inserted->father == inserted->father->father->left){
            u = inserted -> father -> father -> right;
            if(u->color == 'R'){
                inserted->father->color = 'B';
                u -> color = 'B';
                inserted -> father->father->color = 'R';
                inserted = inserted->father->father;
            }
            else{
                if(inserted == inserted->father->right){
                    inserted = inserted->father;
                    LL(inserted);
                }
                RR(inserted->father->father);
                inserted->father->color = 'B';
                inserted->father->father->color = 'R';

            } 
        }else{
            u = inserted->father->father->left;
            if(u->color == 'R'){
                inserted->father->color = 'B';
                u->color = 'B';
                inserted->father->father->color = 'R';
                inserted = inserted->father->father;
            }else{
                if(inserted == inserted->father->left){
                    inserted = inserted -> father;
                    RR(inserted);
                }
                LL(inserted);
                inserted->father->color = 'B';
                inserted->father->father->color = 'R';
            }
        }
    }
    root->color = 'B';
}



node* find_location(node* root, int key){
    node* aux = root;
    node* bef;
    while(aux != NULL){
        if (key > aux -> key){
            bef = aux;
            aux = aux -> right;
        } else if (key < aux -> key) {
            bef = aux;
            aux = aux -> left;
        } else return NULL;
    }
    return bef;
}

void insertion(int key, node* root){
    
    if(root -> key == 0){
        root -> color = 'B';
        root -> key = key;
        return;
    } else {
        node* aux;
        node* new = (node*)malloc(sizeof(node));
        new -> left = NULL;
        new -> right = NULL;
        new -> father = NULL;
        new -> key = key;
        new -> color = 'R';
        aux = find_location(root, key);
        if(aux == NULL){
            printf("Node already inserted!\n");

        } else if(key > aux -> key){ // inseriu à direita
            new -> father = aux;
            aux -> right = new;
            fixup_insertion(root, new);
        }
        else {// inseriu à esquerda
            new -> father = aux;
            aux -> left = new;
            fixup_insertion(root, new);
        }
    }
}

void testaRN(node * root){
    if(root == NULL)
        return;
    else{
        testaRN(root->left);
        printf("Chave: %d\n", root->key);
        printf("Cor: %c\n", root->color);
        testaRN(root->right);
    }
}

int main() {

    node* root = (node*)malloc(sizeof(node));
    root -> left = NULL;
    root -> right = NULL;
    root -> father = NULL;
    root -> key = 0;
    root -> color = 'B';

    insertion(10, root);
    insertion(5, root);
    insertion(15, root);
    insertion(3, root);
    insertion(7, root);
    insertion(12, root);
    insertion(18, root);

    testaRN(root);
    return 0;
}