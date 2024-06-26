#include <iostream>

using namespace std;

int main (){

    int age = 23;
    string freePizza[] = {"Piz1", "Piz2", "Piz3"};

    int *pAge = &age;
    string *pfreePizza = freePizza;

    cout << *pfreePizza;


    return 0;
}