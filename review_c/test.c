#include<stdio.h>
#include<stdlib.h>


int main(int argc, char* argv[]){
	printf("%c\n", ** ++argv);
	printf("%c\n", * ++ *argv );
	return 1;	
}
