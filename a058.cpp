#include <iostream>
using namespace std;
int main()
{
    int n,a=0,b=0,c=0,t;
    cin >> n;
    for (int i=0;i<n;i++){
        cin >> t;
        if (t%3==0){
            a += 1;
        }else if (t%3==1){
            b += 1;
        }else{
            c += 1;
        }
    }
    cout << a << " " << b << " " << c;
}
