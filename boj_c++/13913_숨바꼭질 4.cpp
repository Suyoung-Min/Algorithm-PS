#include<iostream>
#include<cstdio>
#include<utility>
#include<deque>
using namespace std;

int visit[100001]={0,}; // bool 이 아닌 이유= 어떤 pos 에서 왔는지를 저장하기 위함
int main(){
    int n,k;
    scanf("%d %d",&n,&k);

    for(int i=0;i<=100000;i++){
        visit[i]=-1;
    }

    deque<pair<int,int>> dq;
    dq.push_back(make_pair(n,0));
    visit[n]=n;

    int pos,time;
    pair<int,int> cor;
    while(dq.size()){
        cor=dq.front();
        dq.pop_front();

        pos=cor.first,time=cor.second;

        if(pos == k) break;

        if(pos-1 >=0 && visit[pos-1] == -1){
            dq.push_back(make_pair(pos-1,time+1));
            visit[pos-1] = pos;
        }
        if(pos+1 <= 100000 && visit[pos+1] == -1){
            dq.push_back(make_pair(pos+1,time+1));
            visit[pos+1]=pos;
        }
        if(pos*2 <= 100000 && visit[pos*2] == -1){
            dq.push_back(make_pair(pos*2,time+1));
            visit[pos*2]=pos;
        }
    }
    printf("%d\n",time);
    deque<int> ans;
    while(1){
        ans.push_back(pos);
        if(pos == n) break;
        pos = visit[pos];
    }
    for(int i=ans.size()-1;i>=0;i--){
        printf("%d ",ans[i]);
    }
}
