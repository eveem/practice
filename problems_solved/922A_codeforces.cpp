#include <stdio.h>

int main () {
    int copy, real;
    scanf("%d%d", &copy, &real);
    if (real <= 0) {
        printf("No");
    }
    else if (real == 1 && copy != 0) {
        printf("No");
    }
    else if (copy - (real - 1) < 0) {
        printf("No");
    }
    else if ((copy - (real - 1)) % 2 != 0) {
        printf("No");
    }
    else {
        printf("Yes");
    }
}