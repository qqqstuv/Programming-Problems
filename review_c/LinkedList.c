

#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef struct ListNode{
    int val;
    struct ListNode *next;
} ListNode;

void print(ListNode * head){
    printf("Address of head: %p\n", head);
    while(head != NULL){
        printf("%d\n", head->val);
        fflush(stdout);
        head = head->next;  
    }
}

ListNode* init(int val){
    ListNode* node = malloc(sizeof(ListNode));
    node->val =  val;
    node->next = NULL;
    return node;
}

ListNode* create(){
    ListNode * head = NULL;
    ListNode* curr = NULL;
    ListNode* prev = NULL;
    for(int i = 1; i < 10; i++){
        curr = init(i);
        if (prev != NULL){
            prev->next = curr;
        }
        if (head == NULL){
            head = curr;
        }
        prev = curr;
        curr = curr->next;
    }
    return head;
}

void freeList(ListNode* head){
    while(head != NULL){
        ListNode* next = head->next;
        free(head);
        head = next;
    }
}

ListNode* reverse_iterative(ListNode* head){
    ListNode* curr = head->next;
    head->next = NULL;
    ListNode* next = NULL;
    while(curr != NULL){
        next = curr->next;
        curr->next = head;
        head = curr;
        curr = next;
    }
    return head;
}

ListNode* recur_revese(ListNode* curr, ListNode* prev){
    if (curr == NULL){
        return prev;
    } 
    ListNode* next = curr->next;
    curr->next = prev;
    return recur_revese(next, curr);
}

ListNode* reverse_recursive(ListNode* head){
    // ListNode* next = head->next;
    // head->next = NULL;
    ListNode* newHead = recur_revese(head, NULL);
    return newHead;
}

int main(){
    ListNode* head = create();
    print(head);
    head = reverse_iterative(head);
    print(head);
    head = reverse_recursive(head);
    print(head);
    freeList(head);
    
    
    return 0;
}
