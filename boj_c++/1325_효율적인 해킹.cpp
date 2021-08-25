#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;

vector<int> d[10002];
int c[10002]={0,};
bool visit[10002]={0,};
int n,m,a,b;

int bfs(int start){
    queue<int> q;

    for(int i=1;i<=n;i++)
        visit[i]=0;
    
    q.push(start);
    visit[start]=1;

    int t;
    int comp=1;
    while(q.size()){
        t=q.front();
        q.pop();

        for(int i=0;i<d[t].size();i++){
            if(visit[d[t][i]] == 0){
                q.push(d[t][i]);
                visit[d[t][i]]=1;
                comp++;
            }
        }
    }

    return comp;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    
    cin>>n>>m;

    for(int i=0;i<m;i++){
        cin>>a>>b;
        d[b].push_back(a);
    }

    int max=0,tmp;
    for(int i=1;i<=n;i++){
        tmp = bfs(i);
        c[i]=tmp;
        if(max < tmp){
            max = tmp;
        }
    }
    for(int i=1;i<=n;i++){
        if(c[i] == max)
            cout<<i<<' ';
    }
}
