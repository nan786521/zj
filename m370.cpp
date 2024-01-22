#include <iostream>
using namespace std;

int main()
{
    int x,n,t;
    int right=0,left=0,max_postion=-100,min_postion=100;
    cin >> x >> n;
    for (int i=0;i<n;i++){
        cin >> t;
        if (t>x){
            right += 1;
        }else{
            left += 1;
        }
        if (t>max_postion){
            max_postion = t;
        }
        if (t<min_postion){
            min_postion = t;
        }
    }
    if (right>left){
        cout << right << " " << max_postion << endl;
    }else{
        cout << left << " " << min_postion << endl;
    }
}
