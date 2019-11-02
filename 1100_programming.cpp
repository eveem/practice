#include <stdio.h>

unsigned long long int number_basket[20000];

int main()
{
    int n;
    unsigned long long int sum = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int x;
        scanf("%d", &x);
        number_basket[x] += 1;
    }
    for (int i = 0; i < 1001; i++)
    {
        sum += (number_basket[i] * (number_basket[i] - 1)) / 2;

        if (number_basket[i] > 0)
        {
            int a = i / 100;
            int b = (i % 100) / 10;
            int c = i % 10;
            for (int j = i + 1; j < 1001; j++)
            {
                if (number_basket[j] > 0)
                {
                    int aa = j / 100;
                    int bb = (j % 100) / 10;
                    int cc = j % 10;
                    if (a == aa || b == bb || c == cc)
                    {
                        sum += number_basket[i] * number_basket[j];
                    }
                }
            }
        }
    }
    printf("%llu\n", sum);
}