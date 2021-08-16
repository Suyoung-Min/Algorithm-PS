#include<iostream>
#include<cstdio>
using namespace std;

int arr[501]={0,};
int dp[501]={0,};
int main(){
    int n;
    int a,b;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d %d",&a,&b);
        arr[a]=b;
        dp[a]=1;
    }
    int ans=1;
    for(int i=1;i<=500;i++){
        if(arr[i] == 0) continue;
        for(int j=1;j<i;j++){
            if(arr[j] == 0) continue;
            if(arr[j] < arr[i]){
                dp[i]=max(dp[i],dp[j]+1);
                ans = max(ans,dp[i]);
            }
        }
    }
    printf("%d\n",n-ans);
}
//LIS(Longest Increasing Sequence 응용문제
