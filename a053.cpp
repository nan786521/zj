#include <iostream>
using namespace std;
int main()
{
    int n,s;
    cin >> n;
    if (n<=10){
        s=n*6;
    }else if (n<=20){
        s=60+(n-10)*2;
    }else if (n<=40){
        s=80+(n-20)*1;
    }else{
        s=100;
    }
    cout << s;
}
