#include <stdio.h>
#include <string.h>

int main () {
    int n;
    char num[20000];
    scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
        bool result = false;
        scanf("%s", num);
        int len = strlen(num);
        if ((num[len - 1] - '0') % 2 != 0) {
            result = true;
        }
        if (len == 1 && num[0] == '2') {
            result = true;
        }
        if (result) {
            printf("T\n");
        }
        else {
            printf("F\n");
        }
    }
}