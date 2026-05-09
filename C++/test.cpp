#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        long long fact = 1;
        for (int i = 2; i <= N; i++) {
            fact *= i;
        }
        cout << fact << "\n";
    }
    return 0;
}