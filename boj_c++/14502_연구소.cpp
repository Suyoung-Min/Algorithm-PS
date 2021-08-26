#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
#include<cstring>
#include<utility>
using namespace std;

int d[9][9]={0,};
int t[9][9]={0,};
bool visit[9][9]={0,};
int n,m;

int bfs(){
    queue<pair<int,int>> q;
    memset(visit,0,sizeof(visit));

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(t[i][j] == 2){
                q.push(make_pair(i,j));
                visit[i][j]=1;
            }
        }
    }

    pair<int,int> pos;
    int y,x;
    while(q.size()){
        pos=q.front();
        q.pop();

        y=pos.first, x=pos.second;

        if(y-1>=0 && visit[y-1][x] == 0 && t[y-1][x] == 0){
            visit[y-1][x]=1;
            t[y-1][x]=2;
            q.push(make_pair(y-1,x));
        }
        if(y+1 < n && visit[y+1][x] == 0 && t[y+1][x] == 0){
            visit[y+1][x]=1;
            t[y+1][x]=2;
            q.push(make_pair(y+1,x));
        }
        if(x-1 >= 0 && visit[y][x-1] == 0 && t[y][x-1] == 0){
            visit[y][x-1]=1;
            t[y][x-1]=2;
            q.push(make_pair(y,x-1));
        }
        if(x+1 < m && visit[y][x+1] == 0 && t[y][x+1] == 0){
            visit[y][x+1]=1;
            t[y][x+1]=2;
            q.push(make_pair(y,x+1));
        }
    }

    int ret=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(t[i][j] == 0) ret++;
        }
    }

    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n>>m;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++)
            cin>>d[i][j];
    }

    int max_safe=0;
    int tmp;
    for(int i=0;i<=n*m-3;i++){
        for(int j=i+1;j<=n*m-2;j++){
            for(int k=j+1;k<=n*m-1;k++){
                if(d[i/m][i%m] == 0 && d[j/m][j%m] == 0 && d[k/m][k%m] == 0){
                    for(int a=0;a<n;a++){
                        for(int b=0;b<m;b++){
                            t[a][b]=d[a][b];
                        }
                    }
                    t[i/m][i%m]=t[j/m][j%m]=t[k/m][k%m]=1;
                    tmp=bfs();
                    if(max_safe < tmp){
                        max_safe=tmp;
                    }
                }
            }
        }
    }

    cout<<max_safe<<'\n';
}
