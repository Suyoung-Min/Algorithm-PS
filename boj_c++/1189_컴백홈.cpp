#include<iostream>

using namespace std;

char d[6][6];
bool visit[6][6];
int r,c,k;

int dy[4]={-1,0,0,1};
int dx[4]={0,-1,1,0};
int ans;

void dfs(int y,int x,int dist){
    if(y == 0 && x == c-1){
        if(dist == k)
            ans++;
        return;
    }
    if(dist > k) return;
    
    visit[y][x]=true;

    for(int i=0;i<4;i++){
        int ty=y+dy[i];
        int tx=x+dx[i];

        if(ty < 0 || ty >= r || tx < 0 || tx >= c) continue;

        if(visit[ty][tx] == 0 && d[ty][tx] == '.')  dfs(ty,tx,dist+1);
    }

    visit[y][x]=false;
}

int main(){
    cin>>r>>c>>k;
    
    for(int i=0;i<r;i++)
        cin>>d[i];

    dfs(r-1,0,1);
    cout<<ans<<'\n';
}
