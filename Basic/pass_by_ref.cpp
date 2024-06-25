#include <iostream>

using namespace std;
void swap(string &first, string &last);

int main (){

    string first = "Robyn";
    string last = "Batman";
    
    cout << first << last << endl;

    swap(first, last);
    cout << first << last << endl;

    return 0;
}

void swap(string &first, string &last){
    string temp;
    temp = first;
    first = last;
    last = temp;
    
}