#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define N 1000

int part_one(char** input) {
    int gamma_rate = 0, epsilon_rate = 0;
    size_t number_size = strlen(input[0]);
    int* frequency = (int*)calloc(number_size, sizeof(int));

    // Iterate over numbers
    for (int i = 0; i < N; i++)
        // Iterate over number digits
        for (int j = 0; j < number_size; j++) 
            if (input[i][j] == '1') {
                frequency[j]++;
            }

    // Calculate rates based on frequencies
    for (int i = number_size - 1; i >= 0; i--) {
        if (frequency[i] > N / 2)
            gamma_rate += pow(2, number_size - i - 1);

        else 
            epsilon_rate += pow(2, number_size - i - 1);
    }

    return epsilon_rate * gamma_rate;
}

int part_two(char** input) {
    return -1;
}

int main() {
    char* input[N];

    FILE* input_file = fopen("input.txt", "r");
    ssize_t read;
    size_t length = 0;
    char* line;

    for (int i = 0; getline(&line, &length, input_file) != -1; i++) {
        line[strcspn(line, "\n")] = '\0';
        input[i] = strdup(line);
    }

    printf("Part 1: %d\n", part_one(input));
    printf("Part 2: %d\n", part_two(input));

    return 0;
}
