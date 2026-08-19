#include <iostream>
#include <algorithm>
using namespace std;
int arr[101][101]={0,};

int main() {
    // Please write your code here.
    int N,M;
    cin>>N>>M;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin>>arr[i][j];
        }
    }
    int cnt=0;
    for(int i=0; i<N; i++){
        int temp=arr[i][0];
        int temp_cnt=1;
        int max_cnt=0;
        for(int j=1; j<N; j++){
            if(arr[i][j]==temp){
                temp_cnt++;
            }
            else{
                if(max_cnt<temp_cnt){
                   max_cnt=temp_cnt;
                }
                temp_cnt=1;
                temp=arr[i][j];
            }
        }
        if(max_cnt<temp_cnt){
            max_cnt=temp_cnt;
        }
        if(max_cnt>=M){
            cnt++;
        }
    }
    for(int j=0; j<N; j++){
        int temp=arr[0][j];
        int temp_cnt=1;
        int max_cnt=0;
        for(int i=1; i<N; i++){
            if(arr[i][j]==temp){
                temp_cnt++;
            }
            else{
                if(max_cnt<temp_cnt){
                    max_cnt=temp_cnt;
                }
                temp_cnt=1;
                temp=arr[i][j];
            }
        }
        if(max_cnt<temp_cnt){
            max_cnt=temp_cnt;
        }
        if(max_cnt>=M){
            cnt++;
        }
    }
    cout<<cnt;
    return 0;
}