#include <iostream>

using namespace std;

int main (){

    string first = "Robyn";
    string last = "Batman";
    string temp;
    cout << first << last << endl;


    temp = first;
    first = last;
    last = temp;
    cout << first << last << endl;

    return 0;
}