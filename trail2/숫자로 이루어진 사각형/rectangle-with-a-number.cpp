#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin>>N;
    int num=1;
    int arr[N][N];
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            arr[i][j]=num;
            num++;
            if(num==10){
                num=1;
            }
        }
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}