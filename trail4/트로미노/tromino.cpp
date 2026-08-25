#include <iostream>
using namespace std;
int arr[201][201]={0,};
int shape[6][3][2]={
    {{0,0},{1,0},{1,1}},
    {{0,0},{0,1},{1,0}},
    {{0,0},{0,1},{1,1}},
    {{0,1},{1,0},{1,1}},
    {{0,0},{0,1},{0,2}},
    {{0,0},{1,0},{2,0}}
};
int main() {
    // Please write your code here.
    int N,M;
    cin>>N>>M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>arr[i][j];
        }
    }
    int max=-1;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            for(int m=0; m<6; m++){
                int sum=0;
                bool flag=false;
                for(int n=0; n<3; n++){
                    int nc=i+shape[m][n][0];
                    int nr=j+shape[m][n][1];
                    if(nc>=N || nr>=M){
                        flag=true;
                        break;
                    }
                    sum+=arr[nc][nr];
                }
                if(flag==false){
                    if(max<sum) max=sum;
                }
            }
        }
    }
    cout<<max<<endl;
    return 0;
}