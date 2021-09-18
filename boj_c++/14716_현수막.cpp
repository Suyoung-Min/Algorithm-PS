#include<iostream>
#include<queue>

using namespace std;

int m,n;
bool d[252][252];
bool visit[252][252];

int dy[8]={-1,-1,-1,0,0,1,1,1};
int dx[8]={-1,0,1,-1,1,-1,0,1};

void bfs(int a,int b){
    queue<pair<int,int>> q;
    q.push( {a,b} );

    while(!q.empty()){
        int y=q.front().first;
        int x=q.front().second;
        q.pop();

        for(int i=0;i<8;i++){
            int ty=y+dy[i];
            int tx=x+dx[i];

            if(ty < 0 || ty >= m || tx < 0 || tx >= n) continue;

            if(d[ty][tx] == 1 && visit[ty][tx] == false){
                visit[ty][tx] = true;
                q.push( {ty,tx} );
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>m>>n;

    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++)
            cin>>d[i][j];
    }

    int ans=0;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(d[i][j] == 1 && visit[i][j] == false){
                visit[i][j]=true;
                ans++;

                bfs(i,j);
            }
        }
    }

    cout<<ans<<'\n';
}
