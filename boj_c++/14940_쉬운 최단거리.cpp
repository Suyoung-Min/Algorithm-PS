#include<iostream>
#include<queue>
#include<utility>
#include<algorithm>
using namespace std;

int n,m;
int d[1001][1001]={0,};
int t[1001][1001]={0,};
bool visit[1001][1001]={0,};

typedef struct _cor{
    int y;
    int x;
    int dis;
}cor;

void bfs(int a,int b){
    queue<cor> q;
    visit[a][b]=1;
    
    cor pos;
    pos.y=a,pos.x=b,pos.dis=0;
    q.push(pos);
    int y,x,dis;
    while(q.size()){
        pos=q.front();
        q.pop();

        y=pos.y,x=pos.x,dis=pos.dis;
        t[y][x]=dis;

        if(y-1>=0 && visit[y-1][x] == 0 && d[y-1][x] == 1){
            visit[y-1][x]=1;
            pos.x=x,pos.y = y-1,pos.dis=dis+1;
            q.push(pos);
        }
        if(y+1<n && visit[y+1][x] == 0 && d[y+1][x] == 1){
            visit[y+1][x]=1;
            pos.x=x,pos.y = y+1,pos.dis=dis+1;
            q.push(pos);
        }
        if(x-1>=0 && visit[y][x-1] == 0 && d[y][x-1] == 1){
            visit[y][x-1]=1;
            pos.x=x-1,pos.y=y,pos.dis=dis+1;
            q.push(pos);
        }
        if(x+1<m && visit[y][x+1] == 0 && d[y][x+1] == 1){
            visit[y][x+1]=1;
            pos.x=x+1,pos.y=y,pos.dis=dis+1;
            q.push(pos);
        }

    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n>>m;
    int ty,tx;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>d[i][j];
            if(d[i][j] == 2){
                ty=i;
                tx=j;
            }
        }
    }

    bfs(ty,tx);

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(visit[i][j] == 0 && d[i][j] == 1){
                t[i][j]=-1;
            }
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cout<<t[i][j]<<' ';
        }
        cout<<'\n';
    }


}
