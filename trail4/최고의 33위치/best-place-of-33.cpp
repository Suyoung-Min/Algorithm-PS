#include <iostream>
using namespace std;
int arr[20][20]={0,};

int main() {
    // Please write your code here.
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin>>arr[i][j];
        }
    }
    int max_sum=0;
    for(int i=0; i<=N-3; i++){
        for(int j=0; j<=N-3; j++){
            int temp=0;
            for(int m=i; m<i+3; m++){
                for(int n=j; n<j+3; n++){
                    if(arr[m][n]==1){
                        temp++;
                    }
                }
            }
            if(temp>max_sum)
                max_sum=temp;
        }
    }
    cout<<max_sum;
    return 0;
}