#include <iostream>
using namespace std;
int main()
{
    int a,b,c,ans=0;
    for (int i=0;i<5;i++){
        cin >> a >> b >> c;
        if (a+b>c && a+c>b && b+c>a){
            ans+=1;
        }
    }
    cout << ans;
}
