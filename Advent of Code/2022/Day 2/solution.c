#include <stdio.h>
#include <stdlib.h>

char rounds[10000];
int count = 0;

void read_input() {
    FILE* fp = fopen("input.txt", "r");
    char x, y;

    while (EOF != fscanf(fp, "%c %c\n", &x, &y)) {
        rounds[count++] = x;
        rounds[count++] = y;
    }
}

int mod(int a, int b) {
    int r = a % b;

    return r < 0 ? r + b : r;
}

int part_one() {
    int total_score = 0;

    for (int i = 0; i < count; i += 2) {
        int x = (rounds[i] - 'A'),
            y = (rounds[i + 1] - 'X'),
            delta = y - x,
            result = mod((delta + 1), 3) - 1,
            shape_score = 3 * (result + 1),
            outcome_score = y + 1;

        total_score += shape_score + outcome_score;
    }

    return total_score;
}


int main() {
    read_input();

    printf("Part One: %d\n", part_one());

    return 0;
}
