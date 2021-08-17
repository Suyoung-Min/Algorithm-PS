#include<cstdio>
int dp[100001]={0,};
int main(){
    int n;
    scanf("%d",&n);
    dp[1]=3;
    dp[2]=7;
    for(int i=3;i<=n;i++)
        dp[i]=(dp[i-1]*2+dp[i-2])%9901;
    printf("%d",dp[n]);
}
//////////////////////////////////////////
#include<cstdio>

int dp[100001][2]={0,};
int main(){
    int n;
    scanf("%d",&n);
    dp[1][0]=1;
    dp[1][1]=2;
    for(int i=2;i<=n;i++){
        dp[i][0]=(dp[i-1][0]+dp[i-1][1])%9901;
        dp[i][1]=(dp[i-1][0]*2+dp[i-1][1])%9901;
    }
    printf("%d\n",(dp[n][0]+dp[n][1])%9901);
}
