#include <stdio.h>

int main () {
    int n, r = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int c = 0, a;
        for (int j = 0; j < 3; j++) {
            scanf("%d", &a);
            if (a == 1) {
                c += 1;
            }
        }
        if (c > 1) {
            r += 1;
        }
    }
    printf("%d\n", r);
}