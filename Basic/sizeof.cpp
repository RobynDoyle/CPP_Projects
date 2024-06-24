#include <iostream>

using namespace std;

int main (){

    float gpa = 2.3223233;
    string bob = "bob";


    // need to use ' not "" for char???
    char grades[] = {'A', 'B', 'C'};

    string names[] = {"ted", "jack", "dougal", "bob"};


    //cout << sizeof(gpa);
    //cout << sizeof(names);
    // cout << sizeof(gpa);

    cout << sizeof(names)/sizeof(string) << " elements";

}