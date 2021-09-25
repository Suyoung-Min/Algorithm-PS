#include<iostream>
#include<queue>
using namespace std;

int n,x;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n;

    priority_queue<int,vector<int>,greater<int>> pq;

    while(n--){
        cin>>x;
        if(x == 0){
            if(!pq.empty()){
                cout<<pq.top()<<'\n';
                pq.pop();
            }else{
                cout<<"0\n";
            }
        }else if(x > 0){
            pq.push(x);
        }
    }

    return 0;
}
