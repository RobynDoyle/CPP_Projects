
// filling an array with user input
#include <iostream>

using namespace std;

int main (){

    string foods[5];
    int size = sizeof(foods)/sizeof(foods[0]);

    for (int i = 0; i < size; i++){

        cout << "Please enter order number:" << i + 1 << " ";
        getline(cin, foods[i]);

        if (foods[i] == "q"){
            break;
        }

    
    }

    for (string food : foods){
        if (food == "q"){
            break;
        }
        else{
        cout << food << endl;
        }
    }


    return 0;
}