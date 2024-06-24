// sort items in the array
#include <iostream>

using namespace std;
void sort(int nums[], int size);

int main (){

    int nums[] = {1,4,5,3,6,2,8,9,11,10};
    int size = sizeof(nums)/sizeof(nums[0]);

    sort(nums, size);

    for(int element : nums){
        cout << element << " ";
    }

    return 0;
}

void sort(int nums[], int size){
    int temp;
    for(int i = 0; i < size - 1; i++){
        for(int j = 0; j < size - 1; j++){
            if(nums[j] > nums[j+1]){
                temp = nums[j];
                nums[j] = nums[j+1];
                nums[j + 1] = temp;
            }
        }
    }
}