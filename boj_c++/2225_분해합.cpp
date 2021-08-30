#include<iostream>
using namespace std;

int n,k,ret;
int dp[201][201]={0,};

int func(int tn,int tk){
    if(dp[tn][tk] != 0) return dp[tn][tk];

    int ret=0;
    for(int i=0;i<=tn;i++)
        ret=(ret+func(i,tk-1))%1000000000;

    dp[tn][tk]=ret;
    return ret;
}

int main(){
    cin>>n>>k;
    for(int i=0;i<=200;i++) dp[i][1]=1;
    cout<<func(n,k)<<'\n';
}
