#include <exception>
#include <string>
#include "stdlib.h"
#include "stdio.h"

using namespace std;

class BadLengthException : public exception {
    private:
        int n;

    public:
        BadLengthException(int n) {
            this->n = n;
        }

        const char* what() const throw() {
            char* buf = (char*) malloc(256);

            sprintf(buf, "%d", n);

            return buf;     
        }
};   
