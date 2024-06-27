// Recursive approach is slower and uses more memory
// Less code and its cleaner and eaiser to read

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
    if (num > 1){
        return num * factorial(num - 1);
    }
    else{
        return 1;
    }
}
