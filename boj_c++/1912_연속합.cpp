#include<iostream>
#include<cstdio>
using namespace std;
int dp[100001]={0,};
int arr[100001]={0,};
int main(){
    int n;
    int ans;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d",&arr[i]);

    dp[1]=arr[1];
    ans=arr[1];
    for(int i=2;i<=n;i++){
        dp[i]=max(dp[i-1]+arr[i],arr[i]);
        ans = max(ans,dp[i]);
    }
    printf("%d\n",ans);
}
