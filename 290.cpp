#include <iostream>
#include <string>
using namespace std;
int main()
{
  string d;
  int ans=0;
  cin >> d;
  for (int i=0;i<d.size();i++){
    if (i%2==0){
        ans = ans + (d[i]-'0');
    }else{
        ans = ans - (d[i]-'0');
    }

  }
  cout << abs(ans);
}
