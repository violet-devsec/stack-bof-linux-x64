#include <stdio.h>
#include <string.h>

void greet_me()
{
    char name[200];
    show_date();
    printf("Enter your name:");
    gets(name);
    printf("hi %s !\n",name);
  
}

int main(int argc, char *argv[])
{
    greet_me();
    return 0;  
}