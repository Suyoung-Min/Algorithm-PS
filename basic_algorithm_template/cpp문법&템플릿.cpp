#include <bits/stdc++.h>

using namespace std;

int gcd(int a,int b){
    int c;
    while(b != 0){
        c = a%b;
        a=b;
        b=c;
    }
    return a;
}
/*
유클리드 호제법을 이용한 최대공약수 greater common dividor 계산
*/
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
/*
우선순위 큐
오름차순 greater
*/

int main(){

    int a,b;
    cin>>a>>b;
    cout<<gcd(a,b)<<'\n'<<a*b/gcd(a,b);
    return 0;
}
