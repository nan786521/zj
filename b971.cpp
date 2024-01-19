#include <iostream>
using namespace std;
int main()
{
    int a,b,c;
    while (cin >> a >> b >> c){
        if (c<0){
            for (int i=a;i>=b;i=i+c){
                cout << i << " ";
            }
        }else{
            for (int i=a;i<=b;i=i+c){
                cout << i << " ";
            }
        }
        cout << endl;
    }
}
