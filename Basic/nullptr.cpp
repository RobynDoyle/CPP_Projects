#include <iostream>

using namespace std;

int main (){

    int *pointer = nullptr;
    int x = 234;

    pointer = &x;

    if(pointer == NULL){
        "Address is no assigned ";
    } 
    else{
        "Address is assigned ";
    }

    return 0;
}