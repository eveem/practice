#include <stdio.h>

int main () {
    int n;
    double sed = 0.464102, result = 0;
    scanf("%d", &n);
    if (n % 2 == 0) {
        result = n;
    }
    else if (n == 1) {
        result = 2;
    }
    else if (n == 3) {
        result = 3.732051; 
    }
    else {
        result = n + sed;
    }
    printf("%lf\n", result);
}