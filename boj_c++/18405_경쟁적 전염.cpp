#include<iostream>
#include<queue>

using namespace std;

int n,k,s,x,y;
int d[201][201];

int dy[4]={-1,0,0,1};
int dx[4]={0,-1,1,0};

typedef struct _tri{
    int y;
    int x;
    int time;
}tri;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n>>k;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
            cin>>d[i][j];
    }
    cin>>s>>x>>y;

    
    

    queue<tri> q;
    tri t;
    t.time=0;
    for(int v=1;v<=k;v++){
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(d[i][j] == v){
                    t.y=i,t.x=j;
                    q.push(t);
                }
            }
        }
    }

    while(!q.empty()){
        int y=q.front().y;
        int x=q.front().x;
        int time=q.front().time;
        q.pop();

        if(time == s) break;

        for(int i=0;i<4;i++){
            int ty=y+dy[i];
            int tx=x+dx[i];

            if(ty < 0 || ty >= n || tx < 0 || tx >= n) continue;

            if(d[ty][tx] == 0){
                d[ty][tx]=d[y][x];
                t.y=ty,t.x=tx,t.time=time+1;
                q.push(t);
            }
        }
    }


    cout<<d[x-1][y-1]<<'\n';
}
