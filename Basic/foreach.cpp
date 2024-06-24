// for each loop allows to run more dynamically through the array the normal for loop. 

#include <iostream>

using namespace std;

int main (){

    string name[] = {"bob", "bobby", "breda", "tom", "dan", "ted", "bread"};

    for(string student : name){
        cout << student << "\n";
    }
    return 0;
}