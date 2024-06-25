// enter credit card number
// double every second digit from right to left
// split double digit number
//add all the numbers = A
//Add a all odd single digit number from right to left = B
//Sum A + B = C
// IF C is divdable by 10 then its a valid card.

#include <iostream>

using namespace std;

//functions
int getDigit(const int number);
int sumOddDigits(string cardNumber);
int sumEvenDigits(string cardNumber);


int main(){
    string cardNumber;
    int result = 0;

    cout << "Enter a card number: ";
    cin >> cardNumber;

    result = sumEvenDigits(cardNumber) + sumOddDigits(cardNumber); 
    
    if((result % 10) == 0){
        cout << "VALID";
    }
    else{
        cout << "INVALID";
    }
    
    return 0;
}


int getDigit(const int number){
     

    return number % 10 + (number /10 % 10);

}

int sumOddDigits(string cardNumber){

    int sum = 0;
    // the minus 2 is the second last position
    for (int i = cardNumber.size() -1 ; i > 0; i -=2 ){
        sum += cardNumber[i] - '0' ;
    }
    return sum;


}

int sumEvenDigits(string cardNumber){


    int sum = 0;
    // the minus 2 is the second last position
    for (int i = cardNumber.size() -2 ; i > 0; i -=2 ){
        sum += getDigit(cardNumber[i] - '0' * 2);
    }
    return sum;

}

