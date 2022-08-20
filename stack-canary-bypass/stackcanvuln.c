#include <stdio.h>

void greet_me(char *input)
{
  char name[200];
  printf(input);
  printf("\n");
  gets(name);
  printf("Hi there %s !!\n",name);
}

int main(int argc, char *argv[])
{
  greet_me(argv[1]);
  return 0; 
}