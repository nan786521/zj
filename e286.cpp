#include <iostream>
using namespace std;
int main()
{
    int a1,a2,a3,a4; //�D������
    int b1,b2,b3,b4; //�ȶ�����
    int ans=0; //�D���ӧQ+1�A�ȶ��ӧQ-1
    cin >> a1 >> a2 >> a3 >> a4;
    cin >> b1 >> b2 >> b3 >> b4;
    if (a1+a2+a3+a4 > b1+b2+b3+b4){
        ans=ans+1;
    }else if ((a1+a2+a3+a4 < b1+b2+b3+b4)){
        ans=ans-1;
    }
    cout << a1+a2+a3+a4 <<":" << b1+b2+b3+b4 << endl;

    cin >> a1 >> a2 >> a3 >> a4;
    cin >> b1 >> b2 >> b3 >> b4;
    if (a1+a2+a3+a4 > b1+b2+b3+b4){
        ans=ans+1;
    }else if ((a1+a2+a3+a4 < b1+b2+b3+b4)){
        ans=ans-1;
    }
    cout << a1+a2+a3+a4 <<":" << b1+b2+b3+b4 << endl;

    if (ans==0){
        cout << "Tie";
    }else if (ans>=1){
        cout << "Win";
    }else{
        cout << "Lose";
    }
}
