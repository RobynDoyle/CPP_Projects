#include <iostream>
#include <type_traits>
#include <utility>
#include <initializer_list>

template <typename T, typename U>
bool foo(const std::pair<T, U>&pair,
 const std::initializer_list<std::common_type_t<T, U>>& list) {
     if(list.size() != 2) {
         return false;
     }
     auto it = begin(list);
     return pair.first == *it && pair.second == *std::next(it);
}

int main() {
    {
        std::pair<int, int> pair {1, 3};
        std::initializer_list<int> list {1, 2};
        std::cout<<std::boolalpha<<foo(pair, list)<<'\n';
    }
    {
        std::pair<int, int> pair {1, 2};
        std::initializer_list<int> list {1, 2};
        std::cout<<std::boolalpha<<foo(pair, list)<<'\n';
    }
    {
        std::pair<int, int> pair {1, 2};
        std::initializer_list<int> list {1, 2, 3};
        std::cout<<std::boolalpha<<foo(pair, list)<<'\n';
    }
    {
        std::pair<int, char> pair {1, 2}; //common type is int
        std::initializer_list<int> list {1, 2};
        std::cout<<std::boolalpha<<foo(pair, list)<<'\n';
    }
    {
        // std::pair<int, long> pair {1, 2}; //common type is long int
        // std::initializer_list<int> list {1, 2}; //fails template substitution
        // std::cout<<std::boolalpha<<foo(pair, list)<<'\n';
    }
    {
        std::pair<int, long> pair {1, 2}; //common type is long int
        std::initializer_list<long int> list {1, 2}; //same as common type of pair
        std::cout<<std::boolalpha<<foo(pair, list)<<'\n';
    }
    {
        std::pair<int, long> pair {1, 2}; //common type is long int
        if(foo(pair, {1, 2})) {
            std::cout<<"Matched\n";
        }
    }
}