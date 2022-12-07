#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>

#define FLAGSIZE 128

void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  fgets(buf,FLAGSIZE,f);
  puts(buf);
  fflush(stdout);
}

// need to make the malloc size 0 and then we write into the buffer 
char *getComment(char *src, unsigned char len) {
   unsigned char size, malloc_size;
   // don't store the null terminator or newline b/c it is wasteful!
   size = len - 2;
   // leave room so we can add the null terminator later to print
   malloc_size = size+1;
   char *comment = (char *) malloc(malloc_size);
   memcpy(comment,src,size);
   return comment;
}

void readbuf(char *buf, unsigned char len) {
   char *temp=buf;
   unsigned int i;
   char c;
   for (i=0; i<len; i++) {
      c = fgetc(stdin);
      *temp++=c;
      if (c=='\n') break;
   }
   while (c!='\n') {
      c = fgetc(stdin);
   }
}

#define ARRAY_SIZE 100
char *comments[ARRAY_SIZE];
unsigned int sizes[ARRAY_SIZE];

void print_menu() {
   printf("Do you want to:\n(a) Add\n(d) Delete\n(l) List\n(q) Quit?\n");
   fflush(stdout);
}

int main(int argc, char *argv[])
{
   char buf[256];
   int menu;
   char choice;
   unsigned int number;
   int i=0,j;
   bzero(comments,ARRAY_SIZE*sizeof(char *));
   bzero(sizes,ARRAY_SIZE*sizeof(unsigned int));
   while (1) {
      print_menu();
      readbuf(&choice,1);
      switch(choice) {
         case 'a':
            printf("How big will it be?\n");
	    fflush(stdout);
            scanf("%d",&number);
            fgetc(stdin);
            if (number>255) {
               printf("Hacker detected!\n");
	       fflush(stdout);
               exit(0);
            }
            printf("Enter the comment\n");
	    fflush(stdout);
            readbuf(buf,number);
            sizes[i]=number;
            comments[i++]=getComment(buf,number);
            break;
         case 'd': 
            printf("Which one do you want to delete?\n");
	    fflush(stdout);
            scanf("%d",&number);
            fgetc(stdin);
            if (number>=0 && number<i && comments[number]!=NULL) {
               free(comments[number]);
               comments[number]=NULL;
               sizes[number]=0;
            }
            break;
         case 'l':
            for (j=0; j<ARRAY_SIZE; j++) {
               if (comments[j]!=NULL) {
                  // need NULL terminator to print
                  comments[j][sizes[j]]=0;
                  printf("[%d]:0x%x:%s\n",j,comments[j],comments[j]);
               }
            }
            break;
         case 'q':
            exit(0);
            break;
         default:
            printf("Try harder!\n");
            break;
      }  
   }
}
