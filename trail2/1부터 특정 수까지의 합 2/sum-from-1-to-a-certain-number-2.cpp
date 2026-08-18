#include <iostream>
using namespace std;
int N;
int sum=0;

void recursive(int num){
    if(num==0){
        return;
    }
    sum+=num;
    recursive(num-1);
}

int main() {
    // Please write your code here.
    cin>>N;
    recursive(N);
    cout<<sum;
    return 0;
}