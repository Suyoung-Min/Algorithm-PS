#include<iostream>
#include<cstdio>
#include<utility>
#include<deque>
using namespace std;
/*
단순 bfs로 풀었지만 -1,+1,*2 라는 간선 3개가 정점마다 있는 그래프로 취급하고 다익스트라 적용도 가능
*/
bool visit[100001]={0,};
int main(){
    int n,k;
    scanf("%d %d",&n,&k);

    deque<pair<int,int>> dq;
    dq.push_back(make_pair(n,0));
    visit[n]=true;

    int pos,time;
    pair<int,int> cor;
    while(dq.size()){
        cor=dq.front();
        dq.pop_front();

        pos=cor.first,time=cor.second;
        if(pos == k) break;

        if(pos*2 <= 100000 && !visit[pos*2]){
            dq.push_front(make_pair(pos*2,time));
            visit[pos*2]=true;
        }
        if(pos-1 >= 0 && !visit[pos-1]){
            dq.push_back(make_pair(pos-1,time+1));
            visit[pos-1]=true;
        }
        if(pos+1 <= 100000 && !visit[pos+1]){
            dq.push_back(make_pair(pos+1,time+1));
            visit[pos+1]=true;
        }
    }
    printf("%d\n",time);
}
