#include <iostream>
#include <algorithm>
using namespace std;
int N,M;
int arr[6][6]={0,};

int getAreaSum(int sx, int sy, int tx, int ty){
    int sum=0;
    for(int i=sx; i<tx+1; i++){
        for(int j=sy; j<ty+1; j++){
            sum+=arr[i][j];
        }
    }
    return sum;
}

int main() {
    // Please write your code here.
    cin>>N>>M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>arr[i][j];
        }
    }
    int ans=-987654321;
    for(int x1=0; x1<N; x1++){
        for(int y1=0; y1<M; y1++){
            for(int x2=x1; x2<N; x2++){
                for(int y2=y1; y2<M; y2++){

                    for(int x3=0; x3<N; x3++){
                        for(int y3=0; y3<M; y3++){
                            for(int x4=x3; x4<N; x4++){
                                for(int y4=y3; y4<M; y4++){
                                    if(x4<x1 || x2<x3 || y2<y3 || y4<y1){
                                        ans=max(ans, getAreaSum(x1,y1,x2,y2)+getAreaSum(x3,y3,x4,y4));
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    cout<<ans;

    return 0;
}