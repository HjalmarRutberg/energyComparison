#include <stdio.h>
#include <stdlib.h>

// Short sum of squares program that reads in a list of integers from a file 
// and calculates the sum of their squares

void sumOfSquares(int *list, int listSize,long long *result);

int main(int argc, char *argv[]) {
    
    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL) { 
        printf("Error opening file.\n");
        return 1;
    }

    // Find size of input list
    int listSize = 0;
    int temp;
    while (fscanf(fp, "%d", &temp) == 1) {
        listSize++;
    }

    // Rewind filepointer and then read all numbers into an array
    rewind(fp);
    int *list = (int *)malloc(listSize * sizeof(int));
    for (int i = 0; i < listSize; i++) {
        fscanf(fp, "%d", &list[i]);
    }

    int n_loops = atoi(argv[2]);
    for (int i = 0; i < n_loops; i++) {
        // Calculate sum of squares
        long long *result = malloc(sizeof(long long));
        sumOfSquares(list, listSize, result);
        printf("Sum of squares: %lld\n", *result);
        free(result);
    }

    free(list);
    fclose(fp);
    return 0;
}

void sumOfSquares(int *list, int listSize,long long *result) {
    long long sum = 0;
    for (int i = 0; i < listSize; i++) {
        sum += (long long)list[i] * list[i];
    }
    *result = sum;
}