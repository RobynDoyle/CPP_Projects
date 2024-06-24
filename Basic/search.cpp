// search items in an array

#include <iostream>

using namespace std;

int getNum(int num[], int search_num, int size);

int main (){

    int num[] = {1,4,3,65,2,6,7,8,9,10};
    int search_num;
    int size = sizeof(num)/sizeof(int);
    cout << "Number to search: ";
    cin >> search_num;
    int position = getNum(num, search_num, size);

    if(position != -1){
    cout << search_num << " is in position " << position << endl; 
    }
    else{
        cout << "Number is not in this array! " << endl;
    }
    return 0;
}

int getNum(int num[], int search_num, int size){

    for(int i = 0; i < size; i++){
        if (search_num == num[i]){
            return i + 1;
        }

    }
    return -1;
}