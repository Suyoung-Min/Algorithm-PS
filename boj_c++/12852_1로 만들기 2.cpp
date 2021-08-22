#include<iostream>
#include<cstdio>
#include<queue>
#include<utility>
#include<stack>
using namespace std;

int d[1000001][2]={0,};
int main(){
    int n;
    scanf("%d",&n);

    queue<pair<int,int>> q;
    q.push(make_pair(n,0));
    d[n][1]=-1;
    pair<int,int> pos;
    int prev,time;
    while(q.size()){
        pos=q.front();
        q.pop();
        prev = pos.first;
        time = pos.second;

        if(prev == 1) break;

        if(prev%3 == 0 && d[prev/3][1] == 0){
            d[prev/3][1] = prev;
            d[prev/3][0] = time+1;
            q.push(make_pair(prev/3,time+1));
        }
        if(prev%2 == 0 && d[prev/2][1] == 0){
            d[prev/2][1] = prev;
            d[prev/2][0] = time+1;
            q.push(make_pair(prev/2,time+1));
        }
        if(d[prev-1][1] == 0){
            d[prev-1][1]=prev;
            d[prev-1][0]=time+1;
            q.push(make_pair(prev-1,time+1));
        }
    }

    printf("%d\n",d[1][0]);
    stack<int> s;

    int next=1;
    s.push(1);
    while(1){
        if(d[next][1] != -1){
            s.push(d[next][1]);
            next = d[next][1];
        }
        else break;
    }

    while(s.size()){
        printf("%d ",s.top());
        s.pop();
    }
    
}
