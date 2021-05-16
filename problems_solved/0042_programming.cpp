#include <stdio.h>

int main () {
    int n, l;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        long double result = 1;
        scanf("%d", &l);
        for (int j = 0; j < l; j++) {
            result *= 2;
        }
        printf("%.0Lf\n", result);
    }
    return 0;
}