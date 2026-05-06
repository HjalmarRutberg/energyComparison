// Mergesort in C
#include <stdio.h>
#include <stdlib.h>

void mergeSort(int *list, int start, int end);
void merge(int *list, int start, int mid, int end);
int is_sorted(int *list, int size);

int main (int argc, char *argv[]) {

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
    // Sort the list using merge sort
    mergeSort(list, 0, listSize - 1);
    if(is_sorted(list, listSize)) {
        printf("Sort successful\n");
    } else {
        printf("Sort failed\n");
    }

    free(list);
    fclose(fp);
    return 0;
}

void mergeSort(int *list, int start, int end) {
    if (start < end) {
        int mid = start + (end - start) / 2;
        mergeSort(list, start, mid);
        mergeSort(list, mid + 1, end);
        merge(list, start, mid, end);
    }
}

void merge(int *list, int start, int mid, int end) {

    int len1 = mid - start + 1;
    int len2 = end - mid;
    int *leftArr = malloc(len1 * sizeof(int));
    int *rightArr = malloc(len2 * sizeof(int));

    for (int i = 0; i < len1; i++) {
        leftArr[i] = list[start + i];
    }
    for (int j = 0; j < len2; j++) {
        rightArr[j] = list[mid + 1 + j];
    }

    int i = 0, j = 0;
    int k = start;

    while (i < len1 && j < len2) {
        if (leftArr[i] <= rightArr[j]) {
            list[k] = leftArr[i];
            i++;
        } else {
            list[k] = rightArr[j];
            j++;
        }
        k++;
    }

    while (i < len1) {
        list[k] = leftArr[i];
        i++;
        k++;
    }

    while (j < len2) {
        list[k] = rightArr[j];
        j++;
        k++;
    }
}

int is_sorted(int *list, int size) {
    for (int i = 0; i < size - 1; i++) {
        if (list[i] > list[i + 1]) {
            return 0;
        }
    }
    return 1;
}