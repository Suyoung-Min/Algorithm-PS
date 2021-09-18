#include<iostream>
#include<queue>
#include<algorithm>

using namespace std;

int r,c;
char d[252][252];
bool visit[252][252];

int dy[4]={-1,0,0,1};
int dx[4]={0,-1,1,0};

int bfs(int a,int b){
    queue<pair<int,int>> q;
    q.push( {a,b} );

    int tk=0,tv=0;

    while(!q.empty()){
        int y=q.front().first;
        int x=q.front().second;
        q.pop();

        if(d[y][x] == 'k') tk++;
        else if(d[y][x] == 'v') tv++;

        for(int i=0;i<4;i++){
            int ty=y+dy[i];
            int tx=x+dx[i];

            if(ty < 0 || ty >= r || tx < 0 || tx >= c) continue;

            if(d[ty][tx] != '#' && visit[ty][tx] == false){
                visit[ty][tx] = true;
                q.push( {ty,tx} );
            }
        }

    }

    if(tk > tv) return tk;
    else return -tv;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>r>>c;

    for(int i=0;i<r;i++)
        cin>>d[i];

    int k=0,v=0;

    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if(d[i][j] != '#' && visit[i][j] == false){

                visit[i][j]=true;

                int tmp = bfs(i,j);
                if(tmp >= 0) k+=tmp;
                else         v-=tmp;
            }
        }
    }
    cout<<k<<" "<<v<<'\n';

    return 0;
}
