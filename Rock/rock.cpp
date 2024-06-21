#include <iostream>
using namespace std;

int choose(int weapon);
//int showWeapon(int weapon)


int main(){
    int weapon = 0;
    int menu;
    cout << "" << endl;
    cout << "################### ROCK PAPER SCISSORS #################" << endl;
    cout << "" << endl;
    cout << "1 = Play game\n2 = Exit\n" << endl; 
    cout << "Choose Menu option: ";
    cin >> menu;
    cout << "" << endl;
 
    

    switch(menu){
        case 1: weapon += choose(weapon); 
            break;
        case 2: cout << "Thanks for visiting!\n";
            break;
    }

    cout << weapon << endl;

    //cout << choice << endl;
    return 0;

    

}


int choose(int weapon){

    
    cout << "################### CHOOSE WEAPON #######################\n" << endl;   

    cout << "1 = Rock\n2 = Paper\n3 = Scissors\n" << endl; 
    cout << "Weapon choice: ";
    cin >> weapon;
    
    
    
     if(weapon == 1 || weapon == 2 || weapon == 3){
        
        switch(weapon){
            case 1: cout << "Nice, you chose Rock\n";
                break;
            case 2: cout << "Nice, you chose Paper\n";
                break;
            case 3: cout << "Nice, you chose Scissors\n";
                break;          
        }
        return weapon;
    }   
    else {
        cout << "Oh no, you need to enter 1 2 or 3\n";
        return 5;
    }

}

// User choice shoose 1 2 or 3
// computer choice wil be srand(time NULL) % 3 -1 