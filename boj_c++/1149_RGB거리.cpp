#include<iostream>
#include<cstdio>
using namespace std;

int house[1001][3]={0,};
int dp[1001][3]={0,};
int main(){
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d %d %d",&house[i][0],&house[i][1],&house[i][2]);
    }
    for(int i=1;i<=n;i++){
        dp[i][0] = min(dp[i-1][1],dp[i-1][2])+house[i][0];
        dp[i][1] = min(dp[i-1][0],dp[i-1][2])+house[i][1];
        dp[i][2] = min(dp[i-1][0],dp[i-1][1])+house[i][2];
    }
    int ans=dp[n][0];
    ans = min(ans,dp[n][1]);
    ans = min(ans,dp[n][2]);
    printf("%d\n",ans);
}
