#include<iostream>

using namespace std;

int n,k;
int coin[101];
int dp[10001];

int main(){
    cin>>n>>k;

    for(int i=0;i<n;i++)
        cin>>coin[i];

    dp[0]=1;

    for(int i=0;i<n;i++){
        for(int j = 1; j<=k; j++){
            if(j - coin[i] >= 0){
                dp[j]+=dp[j-coin[i]];
            }
        }
    }

    cout<<dp[k]<<'\n';
}
