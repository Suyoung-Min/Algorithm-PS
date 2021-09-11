#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int n,m;
int s,e;

vector<int> d[300001];
bool visit[300001];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n>>m;
    cin>>s>>e;

    for(int i=0;i<m;i++){
        int x,y;
        cin>>x>>y;

        d[x].push_back(y);
        d[y].push_back(x);
    }

    queue<pair<int,int>> q;
    q.push( {s,0} );
    visit[s]=true;
    int time=0;
    while(!q.empty()){
        int pos = q.front().first;
        int dist = q.front().second;
        q.pop();

        if(pos == e){
            time=dist;
            break;
        }

        if(pos - 1 >= 1 && visit[pos-1] == false){
            visit[pos-1]=true;
            q.push( {pos-1,dist+1} );
        }
        if(pos + 1 <= n && visit[pos+1] == false){
            visit[pos+1]=true;
            q.push( {pos+1,dist+1} );
        }

        for(int i=0;i<d[pos].size();i++){
            if(visit[d[pos][i]] == false){
                visit[d[pos][i]] = true;
                q.push( {d[pos][i],dist+1} );
            }
        }
    }

    cout<<time<<'\n';
}
