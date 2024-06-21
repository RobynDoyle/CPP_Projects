#include <iostream>
using namespace std;

int choose(int choice);


int main(){

    int menu;
    int choice;

    cout << "Choose 1 or 2\n 1 = Play game\n 2 = Exit\n" << endl; 
    cin >> menu;

    switch(menu){
        case 1: choose(choice);
            break;
        case 2: cout << "Thanks for visiting!\n";
            break;
    }

    //cout << choice << endl;
    return 0;

    

}


int choose(int choice){

    

    cout << "Choose 1, 2 or 3: 1 = Rock, 2 = Paper, 3 = Scissors" << endl; 
    cin >> choice;
    
     if(choice == 1 || choice == 2 || choice == 3){
        
        switch(choice){
            case 1: cout << "Nice, you chose rock\n";
                break;
            case 2: cout << "Nice, you chose paper\n";
                break;
            case 3: cout << "Nice, you chose scissors\n";
                break;          
        }
        return choice;
    }   
    else {
        cout << "Oh no, you need to enter 1 2 or 3\n";
        return 0;
    }

}

// User choice shoose 1 2 or 3
// computer choice wil be srand(time NULL) % 3 -1 