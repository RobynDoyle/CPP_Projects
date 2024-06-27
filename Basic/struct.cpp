#include <iostream>

using namespace std;

struct student{
    string name;
    double GPA;
    bool enrolled;
};

void printClass(student student);

int main (){

    student student1;
    student1.name = "Bob";
    student1.GPA = 3.4;
    student1.enrolled = true;

    student student2;
    student2.name = "Dan";
    student2.GPA = 2.4;
    student2.enrolled = true;

    printClass(student1);

    return 0;
}

void printClass(student student){

    cout << student.name;

}