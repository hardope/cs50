#include<stdio.h>
#include<cs50.h>

int main(void)
{
    int a = 0;
    do
    {
        a = get_int("Height:  ");
    }
    while (a < 1 || a > 8);
    for (int b = a - 1; b > 0; b--)     //for loop for decrementing so spaces can be printed in a descending manner
    {
        for (int c = 0; c < b; c++)     //for loop for incrementing and printing spaces
       
        {
            printf(" ");
            
        }
        for (int d = 0; d < a - b; d++)     //for loop for printing hashes after spaces
        {
            printf("#");
        }
        printf("  ");
        for (int e = 0; e < a - b; e++)
        {
            printf("#");        //for loop for printing next block of hashe
        }
       
        printf("\n");
    }
    for (int f = 0; f < a; f++)
    {
        printf("#");
    }
    printf("  ");
    for (int g = 0; g < a; g++)
    {
        printf("#");
    }
    printf("\n");
}