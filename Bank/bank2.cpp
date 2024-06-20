#include <iostream>
#include <iomanip>
using namespace std;


void showBalance(double balance);
double deposit();
double withdraw(double balance);

int main(){

    double balance = 0.23;
    int choice;
    
    do{    
        cout << "\n 1: Show balance\n 2: Deposit\n 3: Withdraw\n 4: Exit \n";
        cin.clear();
        fflush(stdin);

        cin >> choice;

        switch(choice){
            case 1: showBalance(balance);
                break;
            case 2: balance += deposit();
                showBalance(balance);
                cout << "\n";
                break;
            case 3: balance -= withdraw(balance);
                showBalance(balance);
                cout << "\n";
                break;
            case 4: cout << "Bye \n";
                break;
            default: cout << "Enter number between 1 and 4";
        }
    }while(choice != 4);
    return 0;
    
    }

void showBalance(double balance){
    cout << "You have $" << setprecision(2) << fixed << balance << endl;
}
double deposit(){

    double amount;
    cout << "Enter your deposit amount: $"; 
    cin >> amount;
    if (amount < 0){
        cout << "You need to enter a positive vaule to deposit ";
        return 0;
    }
    else{
        return amount;
    }   
}

double withdraw(double balance){
    double withdraw_amount;
    cout << "Enter the amount to withdraw: $";
    cin >> withdraw_amount;

    if (withdraw_amount > balance){
        cout << "Not enough funds";
        return 0;
    }
    else if (withdraw_amount < 0){
        cout << "Not a vaild amount";
        return 0;

    }
    else {
        return withdraw_amount;
    }
    
    
    return withdraw_amount;
}