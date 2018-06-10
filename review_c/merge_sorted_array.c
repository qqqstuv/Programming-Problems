

#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
	struct Node* next;
	int val;
} Node;

void add(Node** head, int val){
	if (*head == NULL){
		*head = malloc(sizeof(Node));
		(*head)->next = NULL;
		(*head)->val = val;
		return;
	}
	Node* current = *head;
	while(current != NULL){
		if(current->next == NULL){
			Node* newNode = malloc(sizeof(Node));
			newNode->next = NULL;
			newNode->val = val;
			current->next = newNode;
			return;
		}
		current = current->next;
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

Node* merge(Node* head1, Node* head2){
	Node* newHead = NULL;
	Node* prev_head1 = head1;
	Node* prev_head2 = head2;
	if(head1 == NULL){
		return head2;
	}
	if(head2 == NULL){
		return head1;
	}
	if(head1->val > head2->val){
		newHead = head2;
	}else{
		newHead = head1;
	}
	while(head1 != NULL && head2 != NULL){
		if(head1->val > head2->val){
			while(head2 != NULL && head1->val > head2->val){
				prev_head2 = head2;
				head2 = head2->next;
			}
			prev_head1 = head1;
			head1 = head1->next;
			prev_head2->next = prev_head1;
			if(head2 != NULL){
				prev_head1->next = head2; 
			}
		}else{
			while(head1 != NULL && head1->val <= head2->val){
				prev_head1 = head1;
				head1 = head1->next;
			}
			prev_head2 = head2;
			head2 = head2->next;	
			prev_head1->next = prev_head2;
			if(head1 != NULL){
				prev_head2->next = head1;
			}
		}
	}
	return newHead;
}

void run(int* array1, int* array2, int length1, int length2 ){
	Node* arrptr1;
	Node* arrptr2;
	for(int i = 0; i< length1; i++){
		add(&arrptr1, array1[i]);	
	}
	for(int i = 0; i< length2; i++){
		add(&arrptr2, array2[i]);	
	}
	print(arrptr1);
	print(arrptr2);
	printf("Before merge\n");
	Node* newNode = merge(arrptr1, arrptr2);
	print(newNode);
		
}
		
int main(){
	//int array1[] = {4,6,8,9,12,34,65};
	//int array2[] = {5,6,9,13,45,67,78};	
//	run(array1, array2, sizeof(array1) / sizeof(array1[0]), sizeof(array2) / sizeof(array2[0]));
		
	int array3[] = {10,11,12, 13};
	int array4[] = {5};	
	run(array3, array4, sizeof(array3) / sizeof(array3[0]), sizeof(array4) / sizeof(array4[0]));
	return 1;
}
