#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* multiplyString(char* str, int num){
	int len = strlen(str);
	char* newStr = malloc((len) * sizeof(*str) * num + sizeof(*str) );
	for(int i = 0; i < num; i++){
		strncpy(newStr + i * len, str, len);
	}
	newStr[strlen(str) * num] = '\0';
	return newStr;
}


int main(){
	int maxLength = 100;
	char str[maxLength];
	scanf("%s", str);
	printf("Entered string: %s\n", str);
	int multiply_time = 0;
	scanf("%d", &multiply_time);
	printf("Entered number: %d\n", multiply_time); 
	char* newStr = multiplyString(str, multiply_time);
	printf("%s\n", newStr);
	return 0;

}
