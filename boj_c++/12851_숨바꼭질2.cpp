#include<iostream>
#include<cstdio>
#include<utility>
#include<deque>
using namespace std;
/*
bfs + dp
*/
int visit[100001][2]={0,};
int main(){
    int n,k;
    scanf("%d %d",&n,&k);
    for(int i=0;i<=100001;i++)
        visit[i][0]=int(1e9)+1;

    deque<pair<int,int>> dq;
    dq.push_back(make_pair(n,0));
    visit[n][1]=1;
    int time=0,
    int pos=0;
    int fast=0;
    bool find_k=false;
    pair<int,int> cor;
    while(dq.size()){
        cor = dq.front();
        dq.pop_front();
        
        pos = cor.first, time = cor.second;

        if(!find_k && pos == k){
            find_k = true;
            fast=time;
            continue;
        }

        if(!find_k){
            if(pos-1>=0 && visit[pos-1][0] >= time){
                visit[pos-1][1]++;
                visit[pos-1][0]=time;
                dq.push_back(make_pair(pos-1,time+1));
            }
            if(pos+1<=100000 && visit[pos+1][0] >= time){
                visit[pos+1][1]++;
                visit[pos+1][0]=time;
                dq.push_back(make_pair(pos+1,time+1));
            }
            if(pos*2<=100000 && visit[pos*2][0] >= time){
                visit[pos*2][1]++;
                visit[pos*2][0]=time;
                dq.push_back(make_pair(pos*2,time+1));
            }
        }else if(time > fast){
            break;
        }
    }
    printf("%d\n%d\n",fast,visit[k][1]);
}
