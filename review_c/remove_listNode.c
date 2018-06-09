#include<stdlib.h>
#include<stdio.h>

typedef struct ListNode {
	int val;
	struct	ListNode* next;	
} ListNode;


int removeNode(ListNode** head, int num){
	ListNode* prev = NULL;
	ListNode* curr = *(head);
	if(curr->val == num){
		curr = (*head)->next;
		free(*head);
		(*head) = curr;
		return 1;
	}
	while(curr != NULL){
		if (curr->val == num){
			prev->next = curr->next;
			free(curr);
			return 1;
		}
		prev = curr;
		curr = curr->next;
	}
	return 0;
}

void print(ListNode* head){
	while(head != NULL){
		printf("%d ", head->val);
		head = head->next;	
	}
	printf("\n");
}


ListNode* init (int num){
	ListNode* head = NULL;
	ListNode* curr = NULL;
	ListNode* prev = NULL;
	for(int i = 0; i < num; i++){
		curr = malloc(sizeof(ListNode));

		curr->next = NULL;
		curr->val = i;
		if (prev != NULL){
			prev->next = curr;
		}
		if (head == NULL){
			head = curr;
		}		
		prev = curr;		
	}
	return head;
}


int main(){
	int num = 10;
	
	ListNode* listNode = init(num);
	int remove_char;
	scanf("%d", &remove_char);
	printf("Entered: %d", remove_char);
	if (removeNode(&listNode, remove_char)){
		printf("Removed: %d\n", remove_char);
	}else{
		printf("Don't find: %d\n", remove_char);
	}
	print(listNode);
	
	return 0;
}
