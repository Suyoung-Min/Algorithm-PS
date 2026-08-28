#include <iostream>
#include <algorithm>
using namespace std;
int N, M;
int arr[21][21]={0,};

bool isPlus(int sx,int sy, int tx, int ty){
    for(int i=sx; i<tx+1; i++){
        for(int j=sy; j<ty+1; j++){
            if(arr[i][j]<=0){
                return false;
            }
        }
    }
    return true;
}

int main() {
    // Please write your code here.
    cin>>N>>M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>arr[i][j];
        }
    }
    int max_area=0;
    for(int x1=0; x1<N; x1++){
        for(int y1=0; y1<M; y1++){
            for(int x2=x1; x2<N; x2++){
                for(int y2=y1; y2<M; y2++){
                    if(isPlus(x1,y1,x2,y2)){
                        max_area=max(max_area,(x2-x1+1)*(y2-y1+1));
                    }
                }
            }
        }
    }
    cout<< (max_area>0 ? max_area : -1);
    return 0;
}