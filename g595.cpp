#include <iostream>
using namespace std;

int main()
{
    int n,ans=0;
    int h[200];
    cin >> n;
    h[0]=999;
    for (int i=1;i<=n;i++){
        cin >> h[i];
    }
    h[n+1]=999;
    for (int i=1;i<=n;i++){
        if (h[i] == 0){
            if (h[i-1] > h[i+1]){
                ans=ans+h[i+1];
            }else{
                ans=ans+h[i-1];
            }
        }
    }
    cout << ans;
}
