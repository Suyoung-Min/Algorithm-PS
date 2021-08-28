#include<iostream>
#include<queue>
#include<utility>
using namespace std;

int n,m;
char d[1001][1001]={0,};
bool visit[1001][1001]={0,};
bool flag=false;

void bfs(int a,int b){
    visit[a][b] = 1;
    queue<pair<int,int>> q;
    q.push(make_pair(a,b));
    pair<int,int> pos;
    int y,x;

    while(q.size()){
        pos=q.front();
        q.pop();

        y=pos.first,x=pos.second;

        if(y == m-1){
            flag = true;
            return;
        }

        if(y-1>=0 && visit[y-1][x] == 0 && d[y-1][x] == '0'){
            visit[y-1][x]=1;
            q.push(make_pair(y-1,x));
        }
        if(y+1<m && visit[y+1][x] == 0 && d[y+1][x] == '0'){
            visit[y+1][x]=1;
            q.push(make_pair(y+1,x));
        }
        if(x-1>=0 && visit[y][x-1] == 0 && d[y][x-1] == '0'){
            visit[y][x-1]=1;
            q.push(make_pair(y,x-1));
        }
        if(x+1<n && visit[y][x+1] == 0 && d[y][x+1] == '0'){
            visit[y][x+1]=1;
            q.push(make_pair(y,x+1));
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>m>>n;
    for(int i=0;i<m;i++){
        cin>>d[i];
    }

    for(int i=0;i<n;i++){
        if(d[0][i] == '0' && flag == false) bfs(0,i);
    }

    if(flag) cout<<"YES"<<'\n';
    else cout<<"NO"<<'\n';
}
