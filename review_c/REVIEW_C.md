


char* str = "hello"; // "hello" is immutable so cannot access the index and change the value of hello
sizeof(str) gives the size of the pointer, which is either 4 or 8

char str[] = "hello";
str = "world"; // cannot do this

extern:
1. Declaration can be done any number of times but definition only once.
2. “extern” keyword is used to extend the visibility of variables/functions().
3. Since functions are visible through out the program by default. The use of extern is not needed in function declaration/definition. Its use is redundant.
4. When extern is used with a variable, it’s only declared not defined.
5. As an exception, when an extern variable is declared with initialization, it is taken as definition of the variable as well.

constand vs #defind
defind is a macro. The preprocessor will replace everything with what is defined. Guarantee constness

Storage class
Register: define local variables that should be stored in a register instead of RAM
Static:The static storage class instructs the compiler to keep a local variable in existence during the life-time of the program instead of creating and destroying it each time it comes into and goes out of scope. Therefore, making local variables static allows them to maintain their values between function calls.
The static modifier may also be applied to global variables. When this is done, it causes that variable's scope to be restricted to the file in which it is declared.
In C programming, when static is used on a global variable, it causes only one copy of that member to be shared by all the objects of its class.
Extern:

#define is a C-directive which is also used to define the aliases for various data types similar to typedef but with the following differences −

typedef is limited to giving symbolic names to types only where as #define can be used to define alias for values as well, q., you can define 1 as ONE etc.

typedef interpretation is performed by the compiler whereas #define statements are processed by the pre-processor.

Review:
- printf
%p prints the pointer address

- scanf

- passing arguments to function:
    + passing a struct will copy the value of the whole struct as an argument
    + passing an array will only copy the value of the pointer that points to the first char in the array

- function pointer

- merge sort



sizeof array, struct size at runtime? 
Add 1 while traversing?
Free from index?

Do:
- Fibonacci number
- Questions on pointers, Had to multiply the string by a number and store the repeated string(result) in another string. Eg, str = "dog", result="dogdogodog".  
- Remove a number in a LinkedList
- Binary Search Tree
- Network Protocol  