#include <stdio.h>

#if defined(__linux__)
#include <ncurses.h>
#endif

#if defined(_WIN32) || defined(_WIN64)
#include <conio.h>
#endif

int main() {
    int x, y, z, b;
    printf("\n\n\tSelect one number of pattern: ");
    scanf("%d",&x);
    for(y = 1; y <= x; y++) {
        for(z =1; z <= x; z++) {
            for(b = 1; b <= x; b++) {
                if (y <= z) {
                    printf("%d", &x);
                } else {
                    printf("");
                }
                for(z = x; z <= 1; z--) {
                    if (z <= x) {
                        printf("%d", z);
                    } else {
                        printf("");
                    }
                printf("\n");
                }
            }
        }
    }
    return 0;
}