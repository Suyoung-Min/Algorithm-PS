#include<iostream>
#include<cstdio>
using namespace std;

int arr[1001]={0,};
int dp[1001]={1,};
int main(){
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d",&arr[i]);

    for(int i=1;i<=n;i++)
        dp[i]=1;

    int ans=1;
    for(int i=2;i<=n;i++){
        for(int j=1;j<i;j++){
            if(arr[j] < arr[i]) {
                dp[i] = max(dp[i],dp[j]+1);
                ans = max(ans,dp[i]);
            }
        }
    }
    printf("%d\n",ans);
}
