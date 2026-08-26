#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
struct Data{
    int x,y,dir;
    int sum;
};
int N;
int arr[21][21]={0,};
int dx[4]={-1,-1,1,1};
int dy[4]={1,-1,-1,1};

int rectangle(int c, int r){
    int sum=arr[c][r];
    int max=0;
    queue<Data> q;
    q.push({c,r,0,arr[c][r]});
    while(!q.empty()){
        Data data=q.front(); q.pop();
        if(data.x==c && data.y==r && data.dir==3){
            if(max<data.sum){
                max=data.sum;
            }
            continue;
        }
        int nx=data.x+(dx[data.dir]);
        int ny=data.y+(dy[data.dir]);
        if(nx>=N || ny>=N || nx<0 || ny<0 || arr[nx][ny]==0){
            continue;
        }
        int newSum = (nx==c && ny==r) ? data.sum : data.sum + arr[nx][ny];
        q.push({nx,ny,data.dir,newSum});
        if(data.dir<3){
            q.push({nx,ny,(data.dir+1), newSum});
        }
    }
    return max;
}

int main() {
    // Please write your code here.
    cin>>N;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin>>arr[i][j];
        }
    }
    int max=-1;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            int temp=rectangle(i,j);
            if(temp>max){
                max=temp;
            }
        }
    }
    cout<<max<<endl;





    return 0;
}