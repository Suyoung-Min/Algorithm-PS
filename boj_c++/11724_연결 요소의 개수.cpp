#include<iostream>
#include<queue>
#include<utility
using namespace std;

int n,m;
int d[1001][1001]={0,};
bool visit[1001]={0,};

void bfs(int s){
    queue<int> q;
    q.push(s);
    int t;
    while(q.size()){
        t=q.front();
        q.pop();

        for(int i=1;i<=n;i++){
            if(visit[i] == 0 && d[t][i] == 1){
                visit[i]=1;
                q.push(i);
            }
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n>>m;
    int a,b;
    for(int i=0;i<m;i++){
        cin>>a>>b;
        d[a][b]=d[b][a]=1;
    }
    int ans=0;
    for(int i=1;i<=n;i++){
        if(visit[i] == 0){
            ans++;
            bfs(i);
        }
    }
    cout<<ans<<'\n';
}
