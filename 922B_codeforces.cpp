#include <stdio.h>

int main () {
    int n, count = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            int k = i ^ j;
            if (k > i && k > j && k <=n && k < i + j) {
                count++;
            }
        }
    }
    printf("%d\n", count);
}