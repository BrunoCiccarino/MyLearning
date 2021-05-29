#include <stdio.h>
#include <stdlib.h>

int main(){
    int *mall = malloc(sizeof(int) *3);
    mall[1] = 1;
    printf("%p -> %d", mall, *mall);
    return 0;
}
