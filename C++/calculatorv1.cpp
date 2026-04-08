#include <bits/stdc++.h>
using namespace std;
long long add(long long arr[], int size){
    long long result = 0;
    for(int i = 0; i < size; i++){
        result += arr[i];
    }
    return result;
}   
int main(){
    long long arr[] = {1,2,3,4};
    cout << add(arr, size(arr)) << endl;
    return 0;
}