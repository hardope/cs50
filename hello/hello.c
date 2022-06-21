#include<stdio.h>
#include<cs50.h>

int main(void)

{
    string name = get_string("What's your name? ");     //get user input
    printf("Hello, %s\n", name);    //prints output
}