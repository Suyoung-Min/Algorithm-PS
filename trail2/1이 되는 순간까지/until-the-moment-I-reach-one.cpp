#include <iostream>
using namespace std;
int cnt=0;

int main() {
    // Please write your code here.
    int N;
    cin>>N;
    while(N!=1){
        if(N%2==0){
            N/=2;
            cnt++;
        }
        else if(N%2==1){
            N/=3;
            cnt++;
        }
    }
    cout<<cnt<<endl;
    return 0;
}