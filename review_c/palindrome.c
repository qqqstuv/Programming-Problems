
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct ListNode{
	char val;
	struct ListNode *next;
} ListNode;
void print(ListNode* head);

ListNode* createString(char* string){
	ListNode* head = NULL;
	ListNode* curr = NULL;
	ListNode* prev = NULL;
	for(int i = 0; i < strlen(string);i++){
		curr = malloc(sizeof(ListNode));
		curr->val = string[i];
		curr->next = NULL;
		if(prev != NULL){
			prev->next = curr;	
		}
		if(head == NULL){
			head = curr;
			
		}
		prev = curr;
		curr = curr->next;	
	}
	return head;
}

void print(ListNode* head){
	while(head != NULL){
		printf("%c\n", head->val);
		head = head->next;
	}
}

ListNode* reverse(ListNode* node){
	ListNode* prev = NULL;
	ListNode* curr = NULL;
	ListNode* next = NULL;
	curr = node->next;
	node->next = NULL;
	prev = node;
	while(curr != NULL){
			
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return prev;
}


bool recursiveCheck(ListNode* right, ListNode** left){
	if (right != NULL){
		if (recursiveCheck(right->next, left)){
			if (right->val == (*left)->val){
				(*left) = (*left)->next;
				return true; 	
			}else{
				return false;
			}	
		}else{
			return false;
		}
	}
	return true;
}

// using recursion to check palindrome
bool recurPalindrome2(ListNode* head){
	ListNode* node = head;
	return recursiveCheck(head, &node);
}


// a - b - b - a
// 0   1   2   3
// 1st method: reverse second half of the list
bool  recurPalindrome(ListNode* head){
	bool isPalindrome = true;
	int size = 0;
	ListNode* node = head;
	while(node != NULL ){
		size += 1;
		node = node->next;
	}
	if(size == 1){
		return isPalindrome;
	}	
	int idxToReverse = 0;
	if (size  % 2 == 1){
		idxToReverse = (size + 1) / 2;
	}else{
		idxToReverse = size / 2;
	}
//	printf("size: %d, idxToReverse: %d\n", size, idxToReverse);
	node = head;
	while(idxToReverse != 0){
		idxToReverse -= 1;
		node = node->next;
	}
	// get node to point to the index of the second half part of the string
	ListNode* reversedNode = reverse(node);
//	print(reversedNode);
	ListNode* otherNode = reversedNode; // keep the tail to reverse later
	// compare head to tail up to length of tail
	node = head;
	while(reversedNode != NULL){
		if (reversedNode->val  != node->val){
			isPalindrome = false;
			break;
		}
		reversedNode = reversedNode ->next;
		node = node->next;
	}
	// Reverse to original string
	reversedNode = reverse(otherNode);
//	printf("Back to original string\n");
//	print(head);
	return isPalindrome;
} 


void main(){
	char a[100];
	scanf("%s", a);
	//char* a = "palindrome";
	ListNode* array_a = createString(a);
	bool result = recurPalindrome(array_a);
	printf(result ? "true\n" : "false\n");
	result = recurPalindrome2(array_a);
	printf(result ? "true\n" : "false\n");
}

