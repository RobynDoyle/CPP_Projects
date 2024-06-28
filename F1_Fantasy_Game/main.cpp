#include <iostream>

using namespace std;


string Welcome(string playerName, string ai_one);

int main (){

    // Sets player variable including user and Ai's.
    string playerName;
    string ai_one = "Sam";

    // Runs welcome programme that allows user to choose their name.
    Welcome(playerName, ai_one);
    



    return 0;
}



string Welcome(string playerName, string ai_one){

    
    cout << "\n***********************************************************************************************\n\n";
    cout << "Welcome to F1 fantasy!\n";

    cout << "Enter your player name: ";
    // Takes input for users name.
    cin >> playerName;

    cout << "Your name is " << playerName << endl;

    cout << "Your opponent is " << ai_one << "\n" << endl; 
    
    cout << "***********************************************************************************************\n\n";



    return playerName;
}