#include<iostream>
#include<math.h>

using namespace std;

bool d[1000001];
int m,n;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>m>>n;

    for(int i=2;i<=sqrt(n);i++){
        if(d[i] == 1) continue;

        int t=2;
        while(t*i <= n){
            d[t*i]=1;
            t++;
        }
    }
    d[1]=1;
    for(int i=m;i<=n;i++){
        if(d[i] == 0) cout<<i<<'\n';
    }

}
