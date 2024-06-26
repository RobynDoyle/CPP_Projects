#include <iostream>

using namespace std;

int main (){

    // create a pointer 
    char *pGrades = NULL;
    int size;

    cout << "How many grades are needed?: ";
    cin >> size;
    cout << '\n';

    pGrades = new char[size];

    

    for(int i = 0; i < size; i++){
        cout << "Enter grade number " << i + 1 << " ";
        cin >> pGrades[i]; 
    }

  

    for(int i = 0; i < size; i++){
        cout << pGrades[i] << " ";
    }

    delete[] pGrades;



    return 0;
}