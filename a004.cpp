#include <iostream>
using namespace std;
int main()
{
    int y;
    while (cin >> y){
        if (y%4!=0){
            cout << "���~" << endl;
        }else{
            if (y%100!=0){
                cout << "�|�~" << endl;
            }else{
                if (y%400==0){
                    cout << "�|�~" << endl;
                }else{
                    cout << "���~" << endl;
                }
            }
        }

    }
}
