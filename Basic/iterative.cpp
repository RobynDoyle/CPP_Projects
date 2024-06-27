#include <iostream>

using namespace std;
int factorial(int num);
int main (){
    int num;
    cout << "To what factorial?: ";
    cin >> num;

    cout << factorial(num);


    return 0;
}


int factorial(int num){
    int product = 1;
    for(int i = 1; i <= num; i++){
        product = product * i;

    }
    return product;
}
