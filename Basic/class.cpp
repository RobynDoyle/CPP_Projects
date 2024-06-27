#include <iostream>

using namespace std;


// class is defined with its features. public lets it be accessed from other places. 
class Human{
    public:
        string name;
        string job;
        int age;

        void eat(){
            cout << "THis person is eating\n";
        }

        void drink(){
            cout << "THis person is drinking\n";
        }

        void sleep(){
            cout << "THis person is sleeping\n";
        }
};

int main (){

    Human human1;
    human1.name = "Bob";
    human1.job = "Builder";
    human1.age = 34;

    Human human2;
    human2.name = "Dan";
    human2.job = "Best Builder";
    human2.age = 84;

    cout << human1.job;
    cout << human2.job;

    human1.sleep();

    return 0;
}