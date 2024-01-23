#include <iostream>
using namespace std;
int main()
{
    long int n;
    cin >> n;
    while (n){
        cout << n << endl;
        n = n / 10;
    }
}
