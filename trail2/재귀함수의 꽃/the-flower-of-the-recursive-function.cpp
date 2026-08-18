#include <iostream>
using namespace std;
int N;

void recursive(int num){
    if(num>0){
        cout<<num<<" ";
    }
    if(num<0){
        int tmp=num*(-1);
        if(tmp>N){
            return;
        }
        cout<<tmp<<" ";
    }
    recursive(--num);

}

int main() {
    // Please write your code here.
    cin>>N;
    recursive(N);
    return 0;
}