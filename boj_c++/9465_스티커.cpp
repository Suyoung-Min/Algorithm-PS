#include<iostream>
#include<algorithm>
using namespace std;

int t,n;

int dp[2][100003];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>t;

    for(int j=0;j<t;j++){
        cin>>n;

        for(int i=2;i<n+2;i++){
            cin>>dp[0][i];
        }
        for(int i=2;i<n+2;i++){
            cin>>dp[1][i];
        }

        for(int i=2;i<n+2;i++){
            dp[0][i]=max(dp[1][i-2],dp[1][i-1])+dp[0][i];
            dp[1][i]=max(dp[0][i-2],dp[0][i-1])+dp[1][i];
        }

        cout<<max(dp[0][n+1],dp[1][n+1])<<'\n';

        
    }
}
