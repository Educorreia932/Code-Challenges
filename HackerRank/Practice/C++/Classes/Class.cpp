#include <iostream>
#include <sstream>

using namespace std;

class Student {
    private:
        int age, standart;
        string first_name, last_name;
    
    public:
        void set_age(int age) {
            this->age = age;
        }

        void set_standart(int standart) {
            this->standart = standart;
        }

        void set_first_name(string first_name) {
            this->first_name = first_name;
        }

        void set_last_name(string last_name) {
            this->last_name = last_name;
        }

        int get_age() {
            return age;
        }

        int get_standart() {
            return standart;
        }

        string get_first_name() {
            return first_name;
        }

        string get_last_name() {
            return last_name;
        }

        string to_string() {
            stringstream ss;
            
            ss << age << "," << first_name << "," << last_name << "," << standart;

            return ss.str();
        }
};

int main() {
    int age, standart;
    string first_name, last_name;

    cin >> age >> first_name >> last_name >> standart;

    Student st;
    st.set_age(age);
    st.set_standart(standart);
    st.set_first_name(first_name);
    st.set_last_name(last_name);

    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standart() << "\n";
    cout << "\n";
    cout << st.to_string();
        
    return 0;
}

