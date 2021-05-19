#include <algorithm>
#include <iterator>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

string reverse_words(string str) {
  	string reversed; 
    string word;
    istringstream ss(str); 

    while (ss >> word) {
 	    reverse(word.begin(), word.end());
        reversed += word + " ";
    }

    reversed.erase(reversed.end() - 1);

	return reversed;
}


