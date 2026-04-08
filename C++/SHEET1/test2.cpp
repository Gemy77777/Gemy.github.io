#include <bits/stdc++.h>
using namespace std;

signed main(){
ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
vector <int> v {10, 20 ,1, 9, 30 , 22, 10};
sort(v.begin(), v.end());
for (auto it:v) cout << it << " ";
return 0;
}