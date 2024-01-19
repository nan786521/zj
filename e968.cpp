#include <iostream>
using namespace std;

int main()
{
    int n,t;
    cin >> n;
    int d[n];
    for (int i=0;i<n;i++){
        d[i]=i+1;
    }
    cin >> t;
    d[t-1]=0;
    cin >> t;
    d[t-1]=0;
    cin >> t;
    d[t-1]=0;

    for (int i=n-1;i>=0;i--){
        if (d[i] != 0){
            cout << "No. " << d[i] << endl;
        }
    }
}
