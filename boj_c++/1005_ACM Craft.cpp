#include<iostream>
#include<queue>
#include<vector>

using namespace std;

//dfs + dp , 위상정렬도 가능

int t,n,k,w;
int d[1001];
int dp[1001];

int dfs(vector<vector<int>>& v,int node){
    if(dp[node] >= 0) return dp[node];

    int max=0;
    for(int i=0;i<v[node].size();i++){
        int t;

        if(dp[v[node][i]] >= 0) t = dp[v[node][i]];
        else t= dfs(v,v[node][i]);

        if(max < t) max = t;
    }

    return dp[node]=max+d[node];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>t;

    while(t--){
        cin>>n>>k;

        for(int i=1;i<=n;i++)
            cin>>d[i];

        vector<vector<int>> v;
        v.resize(n+1);

        for(int i=0;i<k;i++){
            int a,b;
            cin>>a>>b;

            v[b].push_back(a);
        }

        for(int i=1;i<=n;i++) dp[i] = -1;

        cin>>w;

        cout<<dfs(v,w)<<'\n';

    }

    return 0;
}
