#include<iostream>
#include<queue>

using namespace std;

int n,k;
int w[100001];
int v[100001];
int dp[101][100001];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n>>k;

    for(int i=1;i<=n;i++){
        cin>>w[i]>>v[i];
    }

    for(int i=1;i<=n;i++){
        for(int j=1;j<=k;j++){
            dp[i][j]=dp[i-1][j];
            if(j-w[i] >= 0)
                dp[i][j]=max(dp[i][j],dp[i-1][j-w[i]]+v[i]);
        }
    }

    cout<<dp[n][k]<<'\n';

    return 0;
}
