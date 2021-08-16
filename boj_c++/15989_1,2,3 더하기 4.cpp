#include<iostream>
#include<cstdio>
using namespace std;

int dp[10001][2]={0,};
int main(){
    int t,n,idx;
    scanf("%d",&t);
    dp[0][0]=1;//3의 배수에서 3으로만 이루어진 경우를 구하기 위한 초기값
    for(int z=0;z<t;z++){
        scanf("%d",&n);

        for(int i=1;i<=n;i++){
            if(dp[i][0] != 0) continue;

            dp[i][0]=1+i/2;
            idx=i;
            while(idx >= 3){
                dp[i][1] += dp[idx-3][0];
                idx-=3;
            }
        }
        printf("%d\n",dp[n][0]+dp[n][1]);
    }
}

/* 라이브러리 가져오는 것도 메모리를 잡아먹는다?
#include<iostream>
#include<cstdio>
using namespace std;

int main(){
    int tc,n,a;
    scanf("%d",&tc);
    while(tc--){
        a=0;
        scanf("%d",&n);
        for(int t=n;t>=0;t-=3){
            a += 1+t/2;
        }printf("%d\n",a);
    }
}
*/
