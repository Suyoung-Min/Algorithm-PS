#include<iostream>

using namespace std;

int n;
int m;

int dp[41];
int fix[41];

int main(){
    cin>>n;
    cin>>m;

    for(int i=0;i<m;i++){
        cin>>fix[i];
    }
    dp[0]=1;
    dp[1]=1;
    int idx=0;
    bool prev_fix_flag=false;
    if(fix[idx] == 1){
        prev_fix_flag = true;
        idx++;
    }

    for(int i=2;i<=n;i++){
        if(i == fix[idx]){
            prev_fix_flag = true;
            dp[i]=dp[i-1];
            idx++;
        }
        else if(prev_fix_flag){
            dp[i]=dp[i-1];
            prev_fix_flag = false;
        }else{
            dp[i]=dp[i-2]+dp[i-1];
        }
    }
    
    cout<<dp[n]<<'\n';
}
