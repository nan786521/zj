#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    vector<string> one,two,three;
    string num;
    int i=0;
    while (cin >> num){
        if (i%3==0){
            one.push_back(num);
        }else if (i%3==1){
            two.push_back(num);
        }else{
            three.push_back(num);
        }

        char ch = getchar();
        if (ch == '\n'){
            break;
        }
        i++;
    }
    for (i=0;i<one.size();i++){
        cout << one[i] << " ";
    }
    cout << endl;
    for (i=0;i<two.size();i++){
        cout << two[i] << " ";
    }
    cout << endl;
    for (i=0;i<three.size();i++){
        cout << three[i] << " ";
    }
}
