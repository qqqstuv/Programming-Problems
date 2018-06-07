

#include <stdio.h>
#include <string.h>


void ptc(){
    char* str1 = "hello"; // pointer to char
    // printf("Size of %d \n", (int) sizeof(str1)  );
    // printf("Size of %d \n", (int) sizeof(str2)  );
    printf("First character %c \n", *str1);
    printf("Second character %c \n", *(str1 + 1) );
    printf("Third character %c \n", *(str1 + 9) );
    printf("Address of first character %p \n", str1);
    printf("Address of pointer str1 %p \n", &str1);
}

void char_array(){
    char str2[] = "hello";

    printf("First char %c\n", str2[0]);
    printf("Second char %c\n", str2[1]);
    printf("Address of char %p\n", str2);
    printf("Address of char %c\n", *(str2  + 1));
    // printf("Address of char %c\n", (str2  + 1));
    
    
    // printf("Address of char %c\n", *(str2 + 1) );
    
    // printf("Second char %c\n", *(&str2) ); 
}

void test_arg(char* c){
    printf("Address passed in is %p\n", c);
    printf("Address of pointer passed in is %p\n", &c);
}

void test_arg2(char c[]){
    printf("Address passed in is %p\n", c);
    printf("Address of pointer passed in is %p\n", &c); 
}

void modified(int i[]){
    i[0] = 10;

}

union Data {
   int i;
   float f;
   char str[20];
} data;

struct A {
    int i;
    float f;
} B;


int main(){

    int a = 10;
    int* b = &a;
    char *c = "hello";
    // printf("Address of int a %p, \n", b);
    // printf("Address of pointer b %p, \n", &b);
    // printf("Address of char c %p \n", c);
    // printf("First char of c: %c or %c \n", c[0], *c);
    // printf("Address of pointer to char c %p \n", &c);
    

    char d[] = "world";
    int i[]= {1,2,3,4,5};
    modified(i);
    // printf("After modified %d \n", i[0]);

    // printf("Size: %d\n", (int) sizeof(union Data) );

    struct B e;

    // test_arg( d);
    // test_arg2(d);
    
    return 0;

}