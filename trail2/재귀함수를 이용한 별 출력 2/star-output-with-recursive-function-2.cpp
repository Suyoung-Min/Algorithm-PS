#include <iostream>
using namespace std;
int N;


void recursive(int num){
    if(num==0){
        return;
    }
    for(int i=0; i<num; i++){
        cout<<"*"<<" ";
    }
    cout<<endl;
    recursive(num-1);
    for(int i=0; i<num; i++){
        cout<<"*"<<" ";
    }
    cout<<endl;
}

int main() {
    // Please write your code here.
    cin>>N;
    recursive(N);
    return 0;
}