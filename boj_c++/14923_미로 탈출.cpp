#include<iostream>
#include<queue>
#include<vector>

using namespace std;

int n,m,Hx,Hy,Ex,Ey;

int d[1001][1001];
bool visit[1001][1001][2];

int dy[4]={-1,0,0,1};
int dx[4]={0,-1,1,0};

typedef struct _cor{
    int y;
    int x;
    bool wall;
    int dist;
}cor;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n>>m;

    cin>>Hy>>Hx;
    cin>>Ey>>Ex;

    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++)
            cin>>d[i][j];
    }

    cor t;
    t.y=Hy,t.x=Hx,t.wall=0,t.dist=0;
    queue<cor> q;
    q.push(t);
    visit[Hy][Hx][0]=1;

    int ans=-1;
    while(!q.empty()){
        int y=q.front().y;
        int x=q.front().x;
        bool wall=q.front().wall;
        int dist=q.front().dist;
        q.pop();

        if(y == Ey && x == Ex){
            ans=dist;
            break;
        }

        if(wall == 0){
            for(int i=0;i<4;i++){
                int ty=y+dy[i];
                int tx=x+dx[i];

                if(ty < 1 || ty > n || tx < 1 || tx > m) continue;

                if((d[ty][tx] == 0 && visit[ty][tx][0] == false) || (d[ty][tx] == 1 && visit[ty][tx][1] == 0)){
                    t.y=ty,t.x=tx,t.wall=d[ty][tx],t.dist=dist+1;
                    visit[ty][tx][t.wall]=1;
                    q.push(t);
                }
                
            }
        }else{
            for(int i=0;i<4;i++){
                int ty=y+dy[i];
                int tx=x+dx[i];

                if(ty < 1 || ty > n || tx < 1 || tx > m) continue;
                
                if(d[ty][tx] == 0 && visit[ty][tx][1] == false){
                    t.y=ty,t.x=tx,t.wall=1,t.dist=dist+1;
                    visit[ty][tx][1]=1;
                    q.push(t);
                }
            }
        }

    }
    
    if(ans == -1)   cout<<"-1\n";
    else            cout<<ans<<'\n';
    
    return 0;
}
