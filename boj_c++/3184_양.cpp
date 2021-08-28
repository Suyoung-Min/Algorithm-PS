#include<iostream>
#include<queue>
#include<utility>
using namespace std;

int r,c;
char d[252][252]={0,};
bool visit[252][252]={0,};

int bfs(int a,int b){

    int sheep=0,wolf=0;

    queue<pair<int,int>> q;
    q.push(make_pair(a,b));
    visit[a][b]=1;

    pair<int,int> pos;
    int y,x;
    while(q.size()){
        pos=q.front();
        q.pop();
        y=pos.first,x=pos.second;

        if(d[y][x] == 'o') sheep++;
        if(d[y][x] == 'v') wolf++;

        if(y-1>=0 && visit[y-1][x] == 0 && d[y-1][x] != '#'){
            visit[y-1][x]=1;
            q.push(make_pair(y-1,x));
        }
        if(y+1<r && visit[y+1][x] == 0 && d[y+1][x] != '#'){
            visit[y+1][x]=1;
            q.push(make_pair(y+1,x));
        }
        if(x-1>=0 && visit[y][x-1] == 0 && d[y][x-1] != '#'){
            visit[y][x-1]=1;
            q.push(make_pair(y,x-1));
        }
        if(x+1<c && visit[y][x+1] == 0 && d[y][x+1] != '#'){
            visit[y][x+1]=1;
            q.push(make_pair(y,x+1));
        }
    }
    if(sheep > wolf) return sheep;
    else return -wolf;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>r>>c;
    for(int i=0;i<r;i++){
        cin>>d[i];
    }

    int sum_sheep=0,sum_wolf=0,tmp;
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if(visit[i][j] == 0 && d[i][j] != '#'){
                tmp=bfs(i,j);
                if(tmp < 0) sum_wolf+=tmp;
                else sum_sheep+=tmp;
            }
        }
    }

    cout<<sum_sheep<<' '<<-sum_wolf<<'\n';
}
