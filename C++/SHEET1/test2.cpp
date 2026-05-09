#include <bits/stdc++.h>
using namespace std;
#define all(v) v.begin(), v.end()

bool cmp(int &a, int &b){
    return a > b;
}

signed main(){
ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
vector <int> v {10, 20 ,1, 9, 30 , 22, 10};
sort(all(v), cmp);
for (auto it:v) cout << it << " ";
return 0;
}