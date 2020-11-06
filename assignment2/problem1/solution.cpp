#include <stdio.h>
#include <stdlib.h>

int num_count;
int array[50000];

int merge(int *array, int *temp, int left, int mid, int right)
{
    int i = left;
    int j = mid;
    int k = left;
    int inv = 0;

    while ((i <= mid-1) && (j <= right))
    {
        if (array[i] <= array[j])
            temp[k++] = array[i++];
        else
        {
            temp[k++] = array[j++];
            inv += mid - i;
        }
    }
    while (i < mid)
        temp[k++] = array[i++];

    while (j <= right)
        temp[k++] = array[j++];

    for (i = left; i <= right; i++)
        array[i] = temp[i];

    return inv;
}

int merge_sort(int *array, int *scratch, int left, int right)
{
    int inv = 0;

    if (left >= right)
        return inv;

    int mid = (left + right) / 2;
    inv += merge_sort(array, scratch, left, mid);
    inv += merge_sort(array, scratch, mid + 1, right);
    inv += merge(array, scratch, left, mid + 1, right);

    return inv;
}

int main(void)
{
    int i;
    scanf("%d", &num_count);
    for (i = 0; i < num_count; i++)
        scanf("%d", &array[i]);

    int *scratch = (int *)malloc(sizeof(int) * num_count);

    int inv = merge_sort(array, scratch, 0, num_count-1);

    printf("%d\n", inv);

    free(scratch); 
    return 0;
}