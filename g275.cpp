#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    int a1,a2,a3,a4,a5,a6,a7;
    int b1,b2,b3,b4,b5,b6,b7;
    string ans;
    cin >> n;
    for (int i=0;i<n;i++){
        ans="";
        cin >> a1 >> a2 >> a3 >> a4 >> a5 >> a6 >> a7;
        cin >> b1 >> b2 >> b3 >> b4 >> b5 >> b6 >> b7;
        if (a2==a4 || b2 == b4 || a2 != a6 || b2 != b6){
            ans=ans + "A";
        }
        if (a7 == 0 || b7 == 1){
            ans=ans + "B";
        }
        if (a2==b2 || a4 == b4 || a6 == b6){
            ans=ans + "C";
        }
        if (ans == ""){
            cout << "None" << endl;
        }else{
            cout << ans << endl;
        }
    }
}
