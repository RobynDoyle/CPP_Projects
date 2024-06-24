#include <iostream>

using namespace std;

int main (){

    string name[] = {"bob", "bobby", "breda", "tom", "dan", "ted"};

    for (int i = 0; i < (sizeof(name)/sizeof(string)); i++){
        cout << name[i] << "\n";
    }


}