// A quiz game using arrays

#include <iostream>

using namespace std;

int main (){

    string questions[] = {"1. When was C++ made?: ",
                        "2. Who invented C++?: ",
                        "3. What came before C++?: ",
                        "4. Is the earth flat?: "};

    string options[][4] = {{"A. 1969", "B. 1975", "C. 1985", "D. 2001"},
                            {"A. tom", "B. Stroustrup", "C. ben", "D. bob"},
                            {"A. C", "B. G++", "C. C+", "D. Python"},
                            {"A. yes", "B. no", "C. maybe", "D. always"}};

    char answerKey[] = {'C', 'B', 'A', 'B'};

    int size = sizeof(questions)/sizeof(questions[0]);
    char guess;
    int score = 0;

    cout << "\n*************************** QUIZ *****************************************\n" << endl;

    for(int i=0; i < size; i++){
        cout << questions[i];

        for(int j = 0; j < sizeof(options[i])/sizeof(options[i][0]); j++){
            cout << options[i][j] << " ";
        }
        cout << "Your Guess = ";
        cin >> guess;
        guess = toupper(guess);

        

        if (guess == answerKey[i]){
            score += 1;
            cout << "Correct! " << "Your score is now " << score << "\n "<< endl;
            
        }
        else{
            cout<< "Wrong! " << "Correct answer was " << answerKey[i] <<". Your score is " << score << "\n " <<  endl;
        }

        cout << "\n**************************************************************************\n" << endl;
    }

    cout << "Overall score = " << score/double(size)*100 << "%" << endl;

    return 0;
}