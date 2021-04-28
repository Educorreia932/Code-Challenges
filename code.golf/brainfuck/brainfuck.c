int main(int argc, char** argv) {
    int array[99999], ptr = 0;

    for (int i = 0; i < argc; i++) {
        switch (argv[i][0]) {
        case '>':
            ptr++;
            break;
        case '<':
            ptr--;
            break;
        case '+':
            array[ptr]++;
            break;
        case '-':
            array[ptr]--;
            break;
        case '.':
            printf("%c", array[ptr]);
            break;
        case '[':
            
            break;
        case ']':
            break;
        }
    } 
}
