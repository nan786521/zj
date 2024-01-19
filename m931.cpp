#include <iostream>
using namespace std;

int main()
{
    int n,a1=0,a2=0,b1=0,b2=0,t1,t2;
    cin >> n;
    for (int i=0;i<n;i++){
        cin >> t1 >> t2;
        if (t1*t1+t2*t2>a1*a1+a2*a2){
            b1=a1;
            b2=a2;
            a1=t1;
            a2=t2;
        }else if (t1*t1+t2*t2>b1*b1+b2*b2){
            b1=t1;
            b2=t2;
        }
    }
    cout << b1 << " " << b2;
}
