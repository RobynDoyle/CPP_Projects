// Allows us to send int or char or double dynamically into the function.

#include <iostream>
// using namespace std; seems that adding this breaks the program???????
template <typename T, typename U>



U max(T x, U y){
    return(x > y) ? x : y;
}

int main(){
    std::cout << max(1, 2.2) << '\n';
    return 0;

}