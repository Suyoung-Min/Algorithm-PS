#include<iostream>
#include<utility>
#include<algorithm>
#include<vector>
#include<cstring>
#include<queue>
using namespace std;
using ll = long long;


int n,start;
vector<int> d[3001];
bool visit[3001],cycle[3001],flag;

void DFS(int now,int cnt){
    for(int i=0;i<d[now].size();i++){
        int next=d[now][i];
        if(cnt >= 2 && start == next){
            flag=true;
            return;
        }
        if(visit[next]) continue;
        visit[next]=true;
        DFS(next,cnt+1);
    }
}

int BFS(int node){
    queue<pair<int,int>> q;
    q.push( {node,0} );
    visit[node]=true;

    while(!q.empty()){
        int now=q.front().first;
        int dis=q.front().second;
        q.pop();

        if(cycle[now]) return dis;

        for(int i=0;i<d[now].size();i++){
            int next=d[now][i];
            if(!visit[next]){
                q.push( {next,dis+1} );
                visit[next]=true;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n;

    int a,b;
    for(int i=0;i<n;i++){
        cin>>a>>b;
        d[a].push_back(b);
        d[b].push_back(a);
    }

    for(int i=1;i<=n;i++){
        start=i;
        visit[start]=true;
        DFS(i,0);
        if(flag) cycle[i] = true;
        flag=false;
        memset(visit,false,sizeof(visit));
    }

    for(int i=1;i<=n;i++){
        if(cycle[i]) cout<<"0 ";
        else{
            cout<<BFS(i)<<" ";
            memset(visit,false,sizeof(visit));
        }
    }


}
