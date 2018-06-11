

#include<stdio.h>
#include<stdlib.h>


int missing_number(int* a, int start,  int end, int length){
	if(length == 1){
		return a[0] == 1 ? 2 : 1;
	}
	int mid = (start + end) / 2;
	printf("%d %d \n", start, end);
	if(start == 0 && end <= 0){
		return a[0] - 1;
	}
	if (a[mid] == mid + 1){ // thing on the right
			
		if (end == start && start == length){
			return a[length] + 1;
		}
		return missing_number(a, mid+1, end, length);
	}else{
		if (a[mid-1] == mid){
			return a[mid] - 1;
		}else{
			return missing_number(a, start, mid-1, length);
		}
	}
	return -1;
}

int main(){
	int a[][2] = {   {1},
			{2}};
	int len = sizeof(a) / sizeof(a[0]);
	for(int i = 0; i < len; i++){
		int eachLength =  sizeof(a[0]) / sizeof(a[0][0]);
		int result = missing_number(a[i], 0, eachLength - 1, eachLength -1) ;
		printf("Result: %d\n", result);
	}
	return 1;
}
