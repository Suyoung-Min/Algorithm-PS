#include<iostream>
#include<queue>

using namespace std;

int d[51][51];
int n,m;
int dy[8]={-1,-1,-1,0,0,1,1,1};
int dx[8]={-1,0,1,-1,1,-1,0,1};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n>>m;

    queue<pair<int,int>> q;

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>d[i][j];
            if(d[i][j] == 1){
                q.push( {i,j} );
            }
        }
    }
    int ans=1;
    while(!q.empty()){
        int y=q.front().first;
        int x=q.front().second;
        q.pop();

        for(int i=0;i<8;i++){
            int ty=y+dy[i];
            int tx=x+dx[i];

            if(ty < 0 || ty >= n || tx < 0 || tx >= m) continue;

            if(d[ty][tx] == 0){
                ans=d[y][x];
                d[ty][tx] = d[y][x]+1;
                q.push( {ty,tx} );
            }
        }
    }

    cout<<ans<<'\n';
    return 0;
}
