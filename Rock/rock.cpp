// Welcome to rock paper scissors file.
// Main menu lets users play or exit. TODO - Add counter for overall wins, losses and draws
// User is promotped to choose a weapon via 1 2 or 3
// Computer choice wil be srand(time NULL) % 3 +1 
// Winner is declared.

#include <iostream>
#include <ctime>
using namespace std;

int choose(int weapon);
int choose_comp_weapon(int comp_weapon);
int who_wins(int weapon, int comp_weapon);
//int showWeapon(int weapon)

//main function
int main(){
    // Set player weapon var
    int weapon = 0;
    int winner = 0;

    // set computer weapon var
    int comp_weapon = 0;
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
        // output the weapon name            
            switch(weapon){
            case 1: cout << "You chose: Rock\n";
                break;
            case 2: cout << "You chose: Paper\n";
                break;
            case 3: cout << "You chose: Scissors\n";
                break;          
        }
        // output the name of weapon that computer chose
            comp_weapon += choose_comp_weapon(comp_weapon);
            switch(comp_weapon){
            case 1: cout << "Computer chose: Rock\n";
                break;
            case 2: cout << "Computer chose: Paper\n";
                break;
            case 3: cout << "Computer chose: Scissors\n";
                break;   
            
            }

            winner += who_wins(weapon, comp_weapon);

            switch(winner){
                case 1: cout << "You win!\n";
                    break;
                case 2: cout << "Computer wins!\n";
                    break;
                case 3: cout << "Draw!\n";
                    break;
            }
            // break out menu
            break;
        case 2: cout << "Thanks for visiting!\n";
            break;
    }

    //cout << choice << endl;
    return 0;
}

//User chooses their weapon
int choose(int weapon){

    
    cout << "################### CHOOSE WEAPON #######################\n" << endl;   

    cout << "1 = Rock\n2 = Paper\n3 = Scissors\n" << endl; 
    cout << "Weapon choice: ";
    cin >> weapon;
    cout << "" << endl;
    
    
    
     if(weapon == 1 || weapon == 2 || weapon == 3){
        /*
        switch(weapon){
            case 1: cout << "Nice, you chose Rock\n";
                break;
            case 2: cout << "Nice, you chose Paper\n";
                break;
            case 3: cout << "Nice, you chose Scissors\n";
                break;          
        }*/
        return weapon;
    }   
    else {
        cout << "Oh no, you need to enter 1 2 or 3\n";
        return 5;
    }

}


// Randomly generated wepaon for computer player
int choose_comp_weapon(int comp_weapon){

    // sets random number generator
    srand(time(NULL));

    // we need 1, 2, or 3. SO we use modulus 3
    int number_of_game_weapons = 3;
    int random_choose_weapon = rand() % number_of_game_weapons +1;

    comp_weapon = random_choose_weapon;
    return comp_weapon;
}

// Calculation for who wins or if its a draw
int who_wins(int weapon, int comp_weapon){

    return 2;
}