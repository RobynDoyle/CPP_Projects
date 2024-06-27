#include <iostream>

using namespace std;

class car{
    public:
        string make;
        string model;
        int year;
        string color;

    car(string make, string model, int year, string color){
        this->make = make;
        this->model = model;
        this->year = year;
        this->color = color;
    }
};

int main (){

    car car1("Honda", "CR2", 2023, "Indigo");
    car car2("Red Bull", "RB19b", 2023, "Matte black");

    cout << car2.make << '\n';
    cout << car2.model << '\n';
    cout << car2.year << '\n'; 
    cout << car2.color << '\n';
    return 0;
}