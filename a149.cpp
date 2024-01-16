#include <iostream>
using namespace std;
int main()
{
    int n;
    long int d,ans;
    cin >> n;
    for (int i=0;i<n;i++){
        ans=1;
        cin >> d;
        if (d==0){
            ans=0;
        }
        while (d){
            ans=ans*(d%10);
            d=d/10;
        }
        cout << ans << endl;
    }
}
