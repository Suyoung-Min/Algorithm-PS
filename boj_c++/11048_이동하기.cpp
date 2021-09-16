#include<iostream>
#include<queue>

using namespace std;

int n,m;
int d[1001][1001];
int dp[1001][1001];

int dy[3]={-1,-1,0};
int dx[3]={-1,0,-1};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n>>m;

    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++)
            cin>>d[i][j];
    }

    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            int max=0;
            for(int t=0;t<3;t++){
                int ty=i+dy[t];
                int tx=j+dx[t];

                if(ty < 1 || ty >n || tx < 1 || tx > m) continue;

                if(max < dp[ty][tx]) max = dp[ty][tx];
            }

            dp[i][j]=max+d[i][j];
        }
    }

    cout<<dp[n][m]<<'\n';

}
