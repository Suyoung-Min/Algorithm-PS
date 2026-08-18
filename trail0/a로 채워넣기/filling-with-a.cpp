#include <iostream>
using namespace std;

int main() {
    string sen="";
    string result="";
    cin>>sen;
    int len=sen.length();
    for(int i=0; i<len; i++){
        if(i==1 || i==len-2){
            result+="a";
        }
        else{
            result+=sen[i];
        }
    }
    cout<<result<<endl;
    return 0;
}