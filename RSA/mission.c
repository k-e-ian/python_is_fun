#include <stdio.h>

/**Find Smallest Divisor , if any, of a given number 'n'
smallest diviser returns if found, Otherwise 0 as is prime*/

int if_division(long unsigned int n)
{
    long unsigned int f;

    if (n % 2 == 0)
    {
        printf("%lu=%lu*%i\n", n, n/2, 2);
        return (0);
    }
    f = 3;
    while (f * f <= n)
    {
        if (n % f == 0)
        {
            printf("%lu=%lu*%lu\n", n, n/f, f);

        }
    }
    printf("%lu=%lu*%i\n", n, n, 1);
    return (0);
}