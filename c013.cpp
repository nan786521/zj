#include <iostream>
using namespace std;
int main()
{
    int n,a,b;
    cin >> n;
    for (int i=0;i<n;i++){ //����ƶq
        cin >> a >> b;
        for (int j=0;j<b;j++){
            for (int k=0;k<a;k++){ //�W�b���Ʀr
                for (int m=0;m<=k;m++){
                    cout << k+1;
                }
                cout << endl;
            }

            for (int k=a-1;k>0;k--){ //�U�b���Ʀr
                for (int m=0;m<k;m++){
                    cout << k;
                }
                cout << endl;
            }
            cout << endl;
        }
    }
}
