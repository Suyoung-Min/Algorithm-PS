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
#include<iostream>
#include<cstdio>
#include<deque>
#include<utility> // pair
using namespace std;
using llint = long long;

int graph[100][100]={0,};
bool visit[100][100]={false,};
int main(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            scanf("%d",&graph[i][j]);
/*
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
            printf("%d ",graph[i][j]);
        printf("\n");
    }
*/
    deque<pair<int,int>> dq;
    if(graph[0][0] != 0) dq.push_back(make_pair(0,0));

    pair<int,int> pos;
    llint ans=0;
    int y,x;
    while(dq.size()){
        pos=dq.front();
        dq.pop_front(); // pop_front는 원소 삭제만 담당, 원소 value 
        y=pos.first,x=pos.second;

        if(y == n-1 && x == n-1){
            ans+=1;
            continue;
        }
        
        if(graph[y][x] == 0 || visit[y][x] == true) continue;

        visit[y][x] = true;
        

        if(y+graph[y][x] <= n-1){
            dq.push_back(make_pair(y+graph[y][x],x));
        }
        if(x+graph[y][x] <= n-1){
            dq.push_back(make_pair(y,x+graph[y][x]));
        }
        
    }
    printf("%lld\n",ans);
}
