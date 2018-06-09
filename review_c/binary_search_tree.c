#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
	int val;
	struct Node* left;
	struct Node* right;
} Node;

void init(Node** node, int val){
	Node* newNode = malloc(sizeof(Node));
	newNode->left = NULL;
	newNode->right = NULL;
	newNode->val = val;
	*node = newNode;
}

void add(Node** head, int val){
	if (*head == NULL){
		init(head, val);
		return;
	}
	Node* curr = *head;
	while(1){
		if (curr->val > val){
			if (curr->left != NULL){
				curr = curr->left;
				continue;
			}else{
				init(&(curr->left), val);
				break;
			}
		}else{
			if(curr->right != NULL){
				curr = curr->right;
				continue;
			}else{
				init(&(curr->right), val);
				break;
			}
		}
	}
}

void in_order_traverse(Node* head){
	if(head != NULL){
		in_order_traverse(head->left);
		printf("%d ", head->val);
		in_order_traverse(head->right);  
	}
}

int main(){
	int a[] = {6,4,2,7,8,3,1,4,5};
	Node* head = NULL;
	int size = sizeof(a) / sizeof(a[0]);
	for(int i = 0; i < size;  i++){
		add(&head, a[i]);
	}
	in_order_traverse(head);
	return 0;
}
