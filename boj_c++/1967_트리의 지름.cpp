#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

// 트리의 지름= 루트에서 가장 먼 정점에서 가장 먼 정점의 길이

int n;
int dist;
int farest;

vector<pair<int,int>> d[10001];
bool visit[10001];

void dfs(int node,int cost){
    if(visit[node]) return;
    visit[node]=true;

    if(dist < cost){
        dist = cost;
        farest=node;
    }

    for(int i=0;i<d[node].size();i++){
        dfs(d[node][i].first,cost+d[node][i].second);
    }

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n;

    for(int i=0;i<n-1;i++){
        int a,b,c;
        cin>>a>>b>>c;

        d[a].push_back( {b,c} );
        d[b].push_back( {a,c} );
    }


    dfs(1,0);
    memset(visit,0,sizeof(visit));
    dist=0;
    dfs(farest,0);

    cout<<dist<<'\n';
}
