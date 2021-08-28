#include<iostream>
#include<queue>
#include<utility>
#include<algorithm>
using namespace std;

int a,b,n,m;
bool visit[100001]={0,};
int main(){
    cin>>a>>b>>n>>m;

    queue<pair<int,int>> q;
    q.push(make_pair(n,0));
    visit[n]=1;
    pair<int,int> pos;
    int x,time;
    while(q.size()){
        pos=q.front();
        q.pop();
        x=pos.first,time=pos.second;

        if(x == m){
            cout<<time<<'\n';
            return 0;
        }

        if(x-1 >= 0 && visit[x-1] == 0){
            visit[x-1]=1;
            q.push(make_pair(x-1,time+1));
        }
        if(x+1 <= 100000 && visit[x+1] == 0){
            visit[x+1]=1;
            q.push(make_pair(x+1,time+1));
        }
        if(x-a >= 0 && visit[x-a] == 0){
            visit[x-a]=1;
            q.push(make_pair(x-a,time+1));
        }
        if(x-b >= 0 && visit[x-b] == 0){
            visit[x-b]=1;
            q.push(make_pair(x-b,time+1));
        }
        if(x+a <= 100000 && visit[x+a] == 0){
            visit[x+a]=1;
            q.push(make_pair(x+a,time+1));
        }
        if(x+b <= 100000 && visit[x+b] == 0){
            visit[x+b]=1;
            q.push(make_pair(x+b,time+1));
        }
        if(x*a <= 100000 && visit[x*a] == 0){
            visit[x*a]=1;
            q.push(make_pair(x*a,time+1));
        }
        if(x*b <= 100000 && visit[x*b] == 0){
            visit[x*b]=1;
            q.push(make_pair(x*b,time+1));
        }
    }
}
