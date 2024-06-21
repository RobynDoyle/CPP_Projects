// Welcome to rock paper scissors file.
// Main menu lets users play or exit. TODO - Add counter for overall wins, losses and draws
// User is promotped to choose a weapon via 1 2 or 3
// Computer choice wil be srand(time NULL) % 3 +1 
// Winner is declared.

#include <iostream>
#include <ctime>
using namespace std;



int choose(int weapon);
int game(int user_total_wins, int computer_total_wins, int total_draws);
int choose_comp_weapon(int comp_weapon);
int who_wins(int weapon, int comp_weapon);
int total_wins(int winner);



//main function
int main(){
    int user_total_wins = 0;
    int computer_total_wins = 0;
    int total_draws = 0;
    game(user_total_wins, computer_total_wins, total_draws);
}


int game(int user_total_wins, int computer_total_wins, int total_draws){
    // Set player weapon var
    int weapon = 0;
    int winner = 0;
    int total_wins;

    // set computer weapon var
    int comp_weapon = 0;
    int menu;
    cout << "" << endl;
    cout << "################### ROCK PAPER SCISSORS #################" << endl;
    cout << "WIN = " << user_total_wins << " LOST = " << computer_total_wins << " DRAW = " << total_draws << endl;  
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
            case 2: cout << "You chose: Scissors\n";
                break;
            case 3: cout << "You chose: Paper\n";
                break;          
        }
        // output the name of weapon that computer chose
            comp_weapon += choose_comp_weapon(comp_weapon);
            switch(comp_weapon){
            case 1: cout << "Computer chose: Rock\n";
                break;
            case 2: cout << "Computer chose: Scissors\n";
                break;
            case 3: cout << "Computer chose: Paper\n";
                break;   
            
            }

            winner += who_wins(weapon, comp_weapon);

            

            switch(winner){
                case 1: cout << "WIN! WIN! WIN! WIN! WIN! WIN! WIN! WIN! WIN! WIN! WIN! WIN! WIN! \n";
                    user_total_wins += 1;
                    break;
                case 2: cout << "LOSE! LOSE! LOSE! LOSE! LOSE! LOSE! LOSE! LOSE! LOSE! LOSE! LOSE! \n";
                    computer_total_wins += 1;
                    break;
                case 3: cout << "DRAW! DRAW! DRAW! DRAW! DRAW! DRAW! DRAW! DRAW! DRAW! DRAW! DRAW! \n";
                    total_draws +=1;
                    break;
            }


            /*

            if (winner == 3){
                total_draws +=1;
                    //break;
                
            }
            else if (winner == 1){
                user_total_wins += 1;
                    //break;
            }
            else {
                computer_total_wins += 1;
                    break;
            }
            
            */
            // loop back to main menu
            return game(user_total_wins, computer_total_wins, total_draws);
            break;
        case 2: cout << "Thanks for visiting!\n" << endl;
        cout << "###################### GAME OVER ########################\n" << endl;
            break;
    }

    //cout << choice << endl;
    return 0;
}

//User chooses their weapon
int choose(int weapon){

    cout << "################### CHOOSE WEAPON #######################\n" << endl;   

    cout << "1 = Rock\n2 = Scissors\n3 = Paper\n" << endl; 
    cout << "Weapon choice: ";
    cin >> weapon;
    cout << "" << endl;
    
     if(weapon == 1 || weapon == 2 || weapon == 3){
        
        return weapon;
    }   
    else {
        cout << "Oh no, you need to enter 1 2 or 3\n";
        return 5;
    }

}

// Randomly generated weapon for computer player
int choose_comp_weapon(int comp_weapon){

    // sets random number generator
    srand(time(nullptr));

    // we need 1, 2, or 3. SO we use modulus 3
    int number_of_game_weapons = 3;
    int random_choose_weapon = rand() % number_of_game_weapons +1;

    comp_weapon = random_choose_weapon;
    return comp_weapon;
}

// Calculation for who wins or if its a draw
int who_wins(int weapon, int comp_weapon){
// rock > scissros > paper > rock 
    if (weapon == 1 && comp_weapon == 1){
        return 3;
    }
    else if (weapon == 2 && comp_weapon == 2){
        return 3;
    }
    else if (weapon == 3 && comp_weapon == 3){
        return 3;
    }
    else if (weapon == 1 && comp_weapon == 2){
        return 1;
    }
    else if (weapon == 2 && comp_weapon == 3){
        return 1;
    }
    else if (weapon == 3 && comp_weapon == 1){
        return 1;
    }
    else if (weapon == 1 && comp_weapon == 3){
        return 2;
    }
    else if (weapon == 2 && comp_weapon == 1){
        return 2;
    }
    else {
        return 2;
    }
}

//count total user wins, computer, and draws
int total_wins(int winner){
    return 6;
}