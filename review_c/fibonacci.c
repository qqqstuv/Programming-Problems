

#include<stdlib.h>
#include<stdio.h>

int fibonacci(int num, int* memo){
	if ( *(memo + num) != -1){
		return *(memo + num);
	}
	int returnVal = -1;
	if (num == 0 || num == 1){
		returnVal = 1;
	}else{
		returnVal = fibonacci(num - 1, memo)  + fibonacci(num - 2, memo);
	}
	*(memo + num) = returnVal;
	return returnVal;
}

int  main(){
	int maxCount = 20;
	int memo[maxCount];
	for(int i = 0; i < maxCount; i ++){
		memo[i] = -1;
	}
	for(int i = 0; i < maxCount; i++){
		printf("%d : %d\n", i, fibonacci(i, memo)); 
	}
	return 0;
}
