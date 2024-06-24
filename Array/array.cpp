//basic array practice

#include <iostream>

using namespace std;

int main (){

    //array with strings
    string car[] = {"nissan", "jeep", "golf", "ferrari"}; 

    //EDIT an item in array
    car[2] = "Lambo\n";

    //index through the array to locate a car
    cout << car[2];

    //array with int
    int age[3];

    age[0] = 1;
    age[1] = 4;
    age[2] = 14;

    cout << age[1];

    return 0;
    

}