#include <iostream>
using namespace std;
int main()
{
    int n,ans=0,t;
    cin >> n;
    for (int i=1;i<=n;i++){
        cin >> t;
        ans = ans + i * t;
    }
    cout << ans;
}
