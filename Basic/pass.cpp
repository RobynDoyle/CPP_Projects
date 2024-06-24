// Pass an array to a function

#include <iostream>

using namespace std;

double getTotal(double prices[], double size);

int main (){

    double prices[] = {49.99, 15.05, 75, 9.99};
    double size = sizeof(prices)/sizeof(double);
    double total_value = getTotal(prices, size);
    cout << total_value << 'endl';

    return 0;
}

double getTotal(double prices[], double size){
    double total = 0;

    for(int i = 0; i < size; i++){
    total += prices[i];
    }

    return total;

}