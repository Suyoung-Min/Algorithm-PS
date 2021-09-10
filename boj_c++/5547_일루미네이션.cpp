#include<iostream>
#include<queue>
#include<algorithm>

using namespace std;

int w,h;

int d[101][101];
bool visit[101][101];

int dy[6]={-1,-1,0,0,1,1};
int dx1[6]={0,1,-1,1,0,1};
int dx2[6]={-1,0,-1,1,-1,0};

void bfsTo2(int a,int b){
    queue<pair<int,int>> q;
    d[a][b]=2;
    q.push( {a,b} );

    while(!q.empty()){
        int y=q.front().first;
        int x=q.front().second;
        q.pop();

        int* dx;
        if(y%2 == 0) dx=dx2;
        else         dx=dx1;

        for(int i=0;i<6;i++){
            int ty=y+dy[i];
            int tx=x+dx[i];

            if(ty < 1 || ty > h || tx < 1 || tx > w) continue;

            if(d[ty][tx] == 0){
                d[ty][tx]=2;
                q.push( {ty,tx} );
            }
        }

    }
}

int func(int y,int x){
    int* dx;
    if(y%2 == 0) dx=dx2;
    else         dx=dx1;
    int ret=0;
    for(int i=0;i<6;i++){
        int ty=y+dy[i];
        int tx=x+dx[i];

        if(ty < 1 || ty > h || tx < 1 || tx > w){
            ret++;
            continue;
        }

        if(d[ty][tx] == 2) ret++;
    }

    return ret;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>w>>h;

    for(int i=1;i<=h;i++){
        for(int j=1;j<=w;j++)
            cin>>d[i][j];
    }

    for(int i=1;i<=w;i++){
        if(d[1][i] == 0) bfsTo2(1,i);
    }
    for(int i=1;i<=w;i++){
        if(d[h][i] == 0) bfsTo2(h,i);
    }
    for(int i=1;i<=h;i++){
        if(d[i][1] == 0) bfsTo2(i,1);
    }
    for(int i=1;i<=h;i++){
        if(d[i][w] == 0) bfsTo2(i,w);
    }

    for(int i=1;i<=h;i++){
        for(int j=1;j<=w;j++){
            if(d[i][j] == 0) d[i][j]=1;
        }
    }
    int ans=0;
    for(int i=1;i<=h;i++){
        for(int j=1;j<=w;j++){
            if(d[i][j] == 1){
                ans+=func(i,j);
            }
        }
    }

    cout<<ans<<'\n';
}
