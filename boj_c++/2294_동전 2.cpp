#include<iostream>

using namespace std;

int n,k;
int coin[101];
int dp[10001];

int main(){
    cin>>n>>k;

    for(int i=0;i<n;i++)
        cin>>coin[i];

    for(int i=0;i<=k;i++){
        dp[i]=int(1e9);
    }
    
    dp[0]=0;

    for(int i=0;i<n;i++){
        for(int j = 1; j<=k; j++){
            if(j - coin[i] >= 0){
                dp[j]=min(dp[j],dp[j-coin[i]]+1);
            }
        }
    }

    if(dp[k] == int(1e9)) cout<<-1<<'\n';
    else                  cout<<dp[k]<<'\n';
}
