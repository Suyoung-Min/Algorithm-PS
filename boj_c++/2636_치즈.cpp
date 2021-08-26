#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
#include<cstring>
#include<utility>
using namespace std;

int d[101][101]={0,};
bool visit[101][101]={0,};
int n,m;

void air_chk(){
    queue<pair<int,int>> q;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++)
            visit[i][j]=0;
    }

    q.push(make_pair(0,0));
    d[0][0]=2;
    visit[0][0]=1;
    pair<int,int> pos;
    int y,x;
    while(q.size()){
        pos=q.front();
        q.pop();
        y=pos.first,x=pos.second;

        if(y-1 >= 0 && visit[y-1][x] == 0 && (d[y-1][x] == 0 || d[y-1][x] == 2)){
            visit[y-1][x]=1;
            d[y-1][x]=2;
            q.push(make_pair(y-1,x));
        }
        if(y+1 < n && visit[y+1][x] == 0 && (d[y+1][x] == 0 || d[y+1][x] == 2) ){
            visit[y+1][x]=1;
            d[y+1][x]=2;
            q.push(make_pair(y+1,x));
        }
        if(x-1 >= 0 && visit[y][x-1] == 0 && (d[y][x-1] == 0 || d[y][x-1] == 2)){
            visit[y][x-1]=1;
            d[y][x-1]=2;
            q.push(make_pair(y,x-1));
        }
        if(x+1 < m && visit[y][x+1] == 0 && (d[y][x+1] == 0 || d[y][x+1] == 2)){
            visit[y][x+1]=1;
            d[y][x+1]=2;
            q.push(make_pair(y,x+1));
        }
    }

}

void printd(){
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++)
            cout<<d[i][j]<<' ';
        cout<<'\n';
    }
}

int cheese_chk(){
    int ret=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++)
            if(d[i][j] == 1) ret++;
    }
    return ret;
}

bool melt_chk(int y,int x){
    bool ret=false;
    if(d[y-1][x] == 2 || d[y+1][x] == 2 || d[y][x-1] == 2 || d[y][x+1] == 2)
        ret = true;
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
    int time=0;
    int prev=0;
    int melt=0;
    while(1){
        if(cheese_chk() == 0){
            break;
        }
        time++;

        queue<pair<int,int>> q;
        melt=0;
        air_chk();
        for(int i=1;i<n;i++){
            for(int j=1;j<m;j++){
                if(d[i][j] == 1){
                    if(melt_chk(i,j)){
                        q.push(make_pair(i,j));
                        melt++;
                    }
                }
            }
        }
        pair<int,int> pos;
        int y,x;
        while(q.size()){
            pos = q.front();
            q.pop();

            y=pos.first, x = pos.second;
            d[y][x] = 2;
        }

    }

    cout<<time<<'\n'<<melt<<'\n';

}
