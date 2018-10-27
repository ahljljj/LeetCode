#include <iostream>
#include <twoSum.h>;
#include <vector>
using namespace std;

int main(){
    
    vector<int> nums {2,7,11,15};
    int target {9};
    twoSum a;
    for(auto i:a.twosum1(nums, target)) cout<<i<<"\t";
    cout << endl;
    return 0;
}

