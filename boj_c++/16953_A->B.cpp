#include<iostream>
#include<queue>
#include<utility>
using namespace std;
using llint = long long;
llint a,b;

int main(){
    cin>>a>>b;

    queue<pair<llint,llint>> q;
    q.push(make_pair(a,1));
    pair<llint,llint> pos;
    llint x,t,ans=-1;
    while(q.size()){
        pos=q.front();
        q.pop();
        x=pos.first,t=pos.second;
        if(x == b){
            ans=t;
            break;
        }

        if(2*x > b){
            continue;
        }

        if(2*x <= b) q.push(make_pair(2*x,t+1));
        if(10*x+1 <= b) q.push(make_pair(10*x+1,t+1));
    }

    cout<<ans<<'\n';
}
