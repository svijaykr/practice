/*
 * =====================================================================================
 *
 *       Filename:  ex1807.c
 *
 *    Description:  1807
 *
 * =====================================================================================
 */
#include <stdio.h>

int main(void)
{
    int n;
    int i,j;

    scanf("%d", &n);

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            if(i  ==0 || j == 0 || i == j)
                printf(" *");
            else
                printf(" 0");
        }
        printf("\n");
    }

    return 0;
}
