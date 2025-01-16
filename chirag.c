#include<stdio.h>

int main()
{   int n;
    printf("Enter Any Day(1-7):");
    scanf("%d",&n);

    switch(n)
    {
        case 1:
               printf("Hello");
               break;

        case 2:
               printf("Bye Everyone");
               break;
            
        default :
               printf("Hello Bhai?");
               break;
    }return 0;
}