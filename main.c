#include <stdio.h>
#include <string.h>
#define MAX_LIMIT 25

char *takeInputFromUser(char *str);
void printStringToNthElement(char *str, int n);

int main()
{
   char str[MAX_LIMIT];
   takeInputFromUser(str);

   int i;
   int len = strlen(str);
   for (i = 0; i < len-1; i++)
   {
      char letter = 'a';
      if(str[i] != ' '){
         while (str[i] != letter)
         {
            printStringToNthElement(str, i);
            printf("%c", letter++);
            printf("\n");
         }
      }
      printStringToNthElement(str, i+1);
      printf("\n");
   }

   return 0;
}

char *takeInputFromUser(char *str)
{
   printf("Enter your input: ");
   fgets(str, MAX_LIMIT, stdin);
   return str;
}

void printStringToNthElement(char *str, int n){
   int i;
   //printf("printing.......... \n");
   for(i =0; i<n; i++){
      printf("%c", str[i]);
   }
}
