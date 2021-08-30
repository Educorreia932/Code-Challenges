#include <math.h>

bool narcissistic(int value) {
    int original_value = value,
        n = 0, 
        num_digits = floor(log10(value) + 1);

    while (value > 0) {
        int digit = value % 10;
        n += pow(digit, num_digits); 
        value /= 10;
    }

    return n == original_value;
}
