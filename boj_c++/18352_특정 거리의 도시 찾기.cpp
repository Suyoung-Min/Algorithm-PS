#include<iostream>
#include<queue>
#include<utility>
#include<algorithm>
using namespace std;



int n,m,k,x;
vector<int> d[300001];
bool visit[300001]={0,};
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n>>m>>k>>x;
    int a,b;
    for(int i=0;i<m;i++){
        cin>>a>>b;
        d[a].push_back(b);
    }

    queue<pair<int,int>> q;
    vector<int> ans;
    q.push(make_pair(x,0));
    visit[x] = 1;
    pair<int,int> pos;
    int point,dis;
    while(q.size()){
        pos = q.front();
        q.pop();

        point=pos.first,dis=pos.second;
        if(dis == k){
            ans.push_back(point);
            continue;
        }

        for(int i=0;i<d[point].size();i++){
            if(visit[d[point][i]] == 0){
                q.push(make_pair(d[point][i],dis+1));
                visit[d[point][i]]=1;
            }
        }

    }

    sort(ans.begin(),ans.end());
    if(ans.size() == 0){
        cout<<-1;
    }
    else{
        for(int i=0;i<ans.size();i++){
            cout<<ans[i]<<'\n';
        }
    }
}
