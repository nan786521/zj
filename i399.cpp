#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a1,a2,a3;
    int d[3];
    cin >> a1 >> a2 >> a3;
    d[0]=a1;
    d[1]=a2;
    d[2]=a3;
    if (a1 == a2 && a2 == a3){
        cout << 3 << " " << a1;
    }else if (a1 == a2 && a1 != a3){
        if (a1 > a3){
            cout << 2 << " " << a1 << " " << a3;
        }else{
            cout << 2 << " " << a3 << " " << a1;
        }
    }else if (a1 == a3 && a1 != a2){
        if (a1 > a2){
            cout << 2 << " " << a1 << " " << a2;
        }else{
            cout << 2 << " " << a2 << " " << a1;
        }
    }else if (a2 == a3 && a2 != a1){
        if (a1 > a2){
            cout << 2 << " " << a1 << " " << a3;
        }else{
            cout << 2 << " " << a3 << " " << a1;
        }
    }else{
        sort(d,d+3);
        cout << 1 << " " << d[2] << " " << d[1] << " " << d[0];
    }
}
