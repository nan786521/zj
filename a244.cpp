#include <iostream>
using namespace std;
int main()
{
    long int n,a,b,c; //�Y�Ʀr�Ӥj�h�ݭn�ŧi��long int(�����)
    cin >> n;
    for (int i=0;i<n;i++){
        cin >> a >> b >> c;
        if (a==1){
            cout << b+c << endl;
        }else if(a==2){
            cout << b-c << endl;
        }else if(a==3){
            cout << b*c << endl;
        }else{
            cout << b/c << endl;
        }
    }
}
