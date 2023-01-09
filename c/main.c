#include<stdio.h>
#include <stdlib.h>

int system(const char *command);

int display(int size, int playerX, int playerY) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (i == playerY && j == playerX) {
                printf("@");
            } else if (i == 0 || i == size - 1 || j == 0 || j == size - 1) {
                printf("#");
            } else {
                printf(" ");
            }

            printf(" ");
        }
        printf("\n");
    }
    return 0;
}

int main() {
    int playerX = 1;
    int playerY = 1;

    int size = 10;

    while (1) {
        system("clear");
        display(size, playerX, playerY);
        char input;
        scanf("%c", &input);

        switch (input) {
            case 'w':
                playerY--;
                break;
            case 's':
                playerY++;
                break;
            case 'a':
                playerX--;
                break;
            case 'd':
                playerX++;
                break;
            case 'q':
                return 0;
        }

        if (playerX > size - 1) {
            playerX = 0;
        } else if (playerX < 0) {
            playerX = size - 1;
        } else if (playerY > size - 1) {
            playerY = 0;
        } else if (playerY < 0) {
            playerY = size - 1;
        }

    }

    // for (int i = 0; i < size; i++) {
    //     display(size, playerPosition);
    //     printf("ok");
    // }

    return 0;
}