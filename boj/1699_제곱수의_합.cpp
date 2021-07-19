#include <iostream>
using namespace std;
int dp[100001];

int main(){
   int n;
   int j;
   cin>>n;
   for(int i=1;i<=n;i++)
      dp[i]=i;
   for(int i=1;i<=n;i++){
      j=1;
      while(j*j<=i){
         if(dp[i-j*j]+1 < dp[i])
            dp[i]=dp[i-j*j]+1;
         j++;
      }
   }
   cout<<dp[n];
}

/*
파이썬과 시간차이 심함
28ms vs 7308ms
*/
