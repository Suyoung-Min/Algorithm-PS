#include<iostream>
#include<cstdio>
using namespace std;

int box[1001]={0,};
int dp[1001]={0,};
int main(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&box[i]);
        dp[i]=1;//하나 선택하는게 기본이므로 dp는 전부 1로 초기화해줘야 함 
    }
    for(int i=1;i<n;i++){
        for(int j=0;j<i;j++)
            if(box[j] < box[i])
                dp[i] = max(dp[j]+1,dp[i]);
    }
    int ans=0;
    for(int i=0;i<n;i++)
        if(dp[i] > ans)
            ans = dp[i];
    printf("%d\n",ans);
}
