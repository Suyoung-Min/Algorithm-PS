#include<iostream>
#include<queue>
#include<algorithm>

using namespace std;

typedef struct _cor{
    int y;
    int x;
    bool flag;
    int dist;
}cor;

int n,m;
int d[1001][1001];
int visit[1001][1001][2];

int dy[4]={0,0,-1,1};
int dx[4]={-1,1,0,0};

int main(){
    
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n>>m;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            char c;
            cin>>c;
            d[i][j]=c-'0';
        }
    }

    queue<cor> q;
    cor t;
    t.y=1,t.x=1,t.flag=0,t.dist=1;
    visit[1][1][0]=1;
    q.push(t);

    int dist0=int(2e9),dist1=int(2e9);

    int y,x,dist,ty,tx;
    bool flag;
    while(!q.empty()){
        y=q.front().y;
        x=q.front().x;
        flag=q.front().flag;
        dist=q.front().dist;
        q.pop();

        if(y == n && x == m){
            if(flag){
                dist1=min(dist1,dist);
            }
            else{
                dist0=min(dist0,dist);
            }
            continue;
        }

        for(int i=0;i<4;i++){
            ty=y+dy[i];
            tx=x+dx[i];

            if(ty <= 0 || ty > n || tx <= 0 || tx > m ) continue;

            if(flag == 0){
                if(d[ty][tx] == 0 && visit[ty][tx][0] == 0){
                    visit[ty][tx][0]=1;
                    t.y=ty,t.x=tx,t.flag=0,t.dist=dist+1;
                    q.push(t);
                }
                if(d[ty][tx] == 1 && visit[ty][tx][1] == 0){
                    visit[ty][tx][1]=1;
                    t.y=ty,t.x=tx,t.flag=1,t.dist=dist+1;
                    q.push(t);
                }
            }else if(flag == 1){
                if(d[ty][tx] == 0 && visit[ty][tx][1] == 0){
                    visit[ty][tx][1] = 1;
                    t.y=ty,t.x=tx,t.flag=1,t.dist=dist+1;
                    q.push(t);
                }
            }
        }
    }

    if(dist0 == int(2e9) && dist1 == int(2e9)){
        cout<<-1<<'\n';
    }
    else{
        cout<<min(dist0,dist1)<<'\n';
    }

}
