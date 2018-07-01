

#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int val;
    struct Node* next;
} Node;


void print(Node* head){
    while(head != NULL){
        printf("%d ", head->val );
        head = head->next;
    }
    printf("\n");
}

Node* reverse_partial(Node* head , int k, Node* tail){
    Node* current = head;  
    Node* prev = NULL;
    Node* next = NULL;
    while(k > 0){ 
        next = current->next;
        current->next = prev;
        prev = current;        
        current = next;
        k -= 1;
    }
    head->next = tail;
    return prev;
}

Node* reverse_k_node(Node* head, int k ){
    Node* newHead = NULL;
    int count = 0;
    Node* traverse = head;
    Node* current = head;
    Node* prev = NULL;
    while(1){
        count = 0;
        
        while(traverse != NULL){
            // printf("Counting: %d, val: %d\n", count, traverse->val);
            traverse = traverse->next;
            count += 1;
            if (count == k){
                // printf("Enough to reverse\n");
                break;
            }
        }
        if (count == k){
            // printf("Reversing node %d\n", current->val);
            current = reverse_partial(current, k, traverse);
            // printf("New current: %d\n", current->val);
            if (prev != NULL){
                prev->next = current;
            }
            if (newHead == NULL){
                newHead = current;
            }
            while(count > 0){
                count -= 1;
                prev = current;
                current = current->next;
            }
            traverse = current;
        }else{
            // printf("Traverse: %d, k: %d\n", traverse->val, k );
            break;
        }
    }
    return newHead;
}
int main(){
    Node a;
    a.val = 1;
    Node b;
    b.val = 2;
    Node c;
    c.val = 3;
    Node d;
    d.val = 4;
    Node e;
    e.val = 5;
    Node f;
    f.val = 6;
    Node g;
    g.val = 7;

    a.next = &b;
    b.next = &c;
    c.next = &d;
    d.next = &e;
    e.next = &f;
    f.next = &g;
    g.next = NULL;
    print(&a);
    Node* newHead = reverse_k_node(&a, 3);
    print(newHead);    
    return 1;
}