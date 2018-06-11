

#include<stdio.h>
#include<stdlib.h>


typedef struct Node{
	int val;
	struct Node* next;
} Node;

Node* init(int val){
	Node* newNode = malloc(sizeof(Node));
	newNode->val = val;
	newNode->next = NULL;
	return newNode;
}

Node* reverse(Node* head){
	Node* curr = head->next;
	Node* prev = head;
	Node* next = NULL;
	head->next = NULL;
	while(curr != NULL){
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next; 
	}
	return prev;
}

void add(Node** node, int val){
	if(*node == NULL){
		*node = init(val);
		return;
	}
	Node* current = *node;
	while(current != NULL){
		if (current->next == NULL){
			current->next = init(val);
			return;
		}
		current = current ->next;
	}
	return;
}

void print(Node* head){
	while(head != NULL){
		printf("%d ", head->val);
		head = head->next;
	}
	printf("\n");
}

int main(){
	Node* head = NULL;
	add(&head, 2);
	add(&head, 3);
	add(&head, 4);
	add(&head, 1);
	print(head);
	head = reverse(head);
	print(head);
	return 1;
}
