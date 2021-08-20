#include<iostream>
#include<cstdio>
#include<utility>
#include<deque>
using namespace std;


int map[301][301]={0,};
bool visit[301][301]={0,};
void ice_bfs(int i,int j){
    deque<pair<int,int>> dq;
    dq.push_back(make_pair(i,j));
    visit[i][j] = true;

    pair<int,int> pos;
    int x,y;
    while(dq.size()){
        pos=dq.front();
        dq.pop_front();
        y=pos.first, x=pos.second;

        if(!visit[y+1][x] && map[y+1][x] != 0){
            dq.push_back(make_pair(y+1,x));
            visit[y+1][x]=true;
        }
        if(!visit[y-1][x] && map[y-1][x] != 0){
            dq.push_back(make_pair(y-1,x));
            visit[y-1][x]=true;
        }
        if(!visit[y][x+1] && map[y][x+1] != 0){
            dq.push_back(make_pair(y,x+1));
            visit[y][x+1]=true;
        }
        if(!visit[y][x-1] && map[y][x-1] != 0){
            dq.push_back(make_pair(y,x-1));
            visit[y][x-1]=true;
        }
    }
}

void ice_melting(int i,int j){
    if(map[i+1][j] == 0) map[i][j]--;
    if(map[i-1][j] == 0) map[i][j]--;
    if(map[i][j+1] == 0) map[i][j]--;
    if(map[i][j-1] == 0) map[i][j]--;
    if(map[i][j]<=0) map[i][j]=-1;
}

int main(){
    int n,m;
    scanf("%d %d",&n,&m);

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++)
            scanf("%d",&map[i][j]);
    }

    int year=0;
    int ice_num=0;
    bool all_melting=false;

    while(1){
        for(int i=1;i<=n-2;i++){
            for(int j=1;j<=m-2;j++)
                if(map[i][j] == -1) map[i][j] = 0;
        }

        for(int i=1;i<=n-2;i++)
            for(int j=1;j<=m-2;j++)
                visit[i][j]=0;
      
      //분리되지 않고 다 녹을 경우
        all_melting=true;
        for(int i=1;i<=n-2;i++){
            for(int j=1;j<=m-2;j++){
                if(map[i][j] != 0){
                    all_melting=false;
                    break;
                }
            }
            if(!all_melting) break;
        }

        if(all_melting){
            year=0;
            break;
        }

        ice_num=0;
        for(int i=1;i<=n-2;i++){
            for(int j=1;j<=m-2;j++){
                if( !visit[i][j] && map[i][j] != 0 ){
                    ice_num++;
                    ice_bfs(i,j);
                }
            }
        }

        if(ice_num >= 2) break;

        year++;

        for(int i=1;i<=n-2;i++){
            for(int j=1;j<=m-2;j++){
                if(map[i][j] == 0 || map[i][j] == -1)  continue;

                ice_melting(i,j);
            }
        }
    }
    printf("%d\n",year);
}
