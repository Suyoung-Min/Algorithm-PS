#include<iostream>
#include<cstdio>
using namespace std;
using llint = long long;

int graph[100][100]={0,};
llint dp[100][100]={0,};
int main(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            scanf("%d",&graph[i][j]);

    dp[0][0]=1;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(graph[i][j] == 0) continue;

            if(i+graph[i][j] <= n-1) dp[i+graph[i][j]][j]+=dp[i][j];
            if(j+graph[i][j] <= n-1) dp[i][j+graph[i][j]]+=dp[i][j];
        }
    }
    printf("%lld\n",dp[n-1][n-1]);
}

// dfs,bfs로 하면 좌표 deque에 좌표가 기하급수적으로 증가하여 메모리 초과, visit 확인하는 문제가 아니므로 사용하기 힘듬
