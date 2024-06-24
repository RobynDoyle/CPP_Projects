// arrays in a grid, with 3 columnns

#include <iostream>

using namespace std;

int main (){


    string car[][3] = {{"Mustang", "Escort", "Fiesta"},
                        {"Alhambra", "Tuscon", "Seat"},
                        {"Golf", "Passat", "Touraeg"}};

    //cout << car[1][1];

    int rows = sizeof(car)/sizeof(car[0]);
    int columns = sizeof(car[0])/sizeof(car[0][0]);

    for (int i = 0; i < rows; i++){
        for(int j = 0; j < columns; j++){
            cout << car[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}