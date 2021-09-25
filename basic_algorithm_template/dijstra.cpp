#include<iostream>
#include<queue>
#include<vector>

using namespace std;

int V,e;
int start;
vector<vector<pair<int,int>>> g;//graph
int d[20001];//distance

struct cmp{
    bool operator()(pair<int,int> a,pair<int,int> b){
        if(a.second > b.second)
            return true;
        else return false;
    }
};



int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>V>>e;

    cin>>start;

    g.resize(V+1);

    while(e--){
        int u,v,w;

        cin>>u>>v>>w;

        g[u].push_back( {v,w} );

    }
    for(int i=1;i<=V;i++){
        d[i]=int(2e9);
    }
    d[start]=0;

    priority_queue<pair<int,int>,vector<pair<int,int>>,cmp> pq;
    pq.push( {start,0} );

    while(!pq.empty()){
        int now = pq.top().first;
        int dist = pq.top().second;
        pq.pop();

        if(d[now] < dist) continue;

        for(int i=0;i<g[now].size();i++){
            pair<int,int> node=g[now][i];

            int cost = dist + node.second;
            
            if(cost < d[node.first]){
                d[node.first]=cost;
                pq.push( {node.first,cost} );
            }
        }
    }

    for(int i=1;i<=V;i++){
        if(d[i] == int(2e9)) cout<<"INF"<<'\n';
        else                 cout<<d[i]<<'\n';
    }
    
    return 0;
}
