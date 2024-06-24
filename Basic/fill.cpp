#include <iostream>

using namespace std;

int main (){
    int size = 99;
    string food[100];

    fill(food, food + (size/3) , "pizza \n");
    fill(food + (size/3), food + (size/3)*2 , "spuds \n");
    fill(food + (size/3)*2, food + size, "cake \n");

    for(int i = 0; i < sizeof(food)/sizeof(food[0]); i++){
    cout << food[i];
    }


    return 0;
}