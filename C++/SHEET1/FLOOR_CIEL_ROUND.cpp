#include <bits/stdc++.h>
using namespace std;
int main(){
int a, b;
cin >> a >> b;
cout <<"floor " << a << " / " << b << " = " << floor((double)a / (double)b) << endl;
cout <<"ceil " << a << " / " << b << " = " << ceil((double)a / (double)b) << endl;
cout <<"round " << a << " / " << b << " = " << round((double)a / (double)b) << endl;
return 0;
}