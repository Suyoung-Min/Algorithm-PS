#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin>>N;
    vector<int> num;
    int temp;
    for(int i=0 ;i<N; i++){
        cin>>temp;
        num.push_back(temp);
    }
    for(int i=N-1; i>=0; i--){
        if(num[i]%2==0){
            cout<<num[i]<<" ";
        }
    }
    return 0;
}