#include<iostream>
#include<queue>
using namespace std;
using llint = long long;

llint a,b,c;
int main(){
    cin>>a>>b>>c;

    queue<llint> bi;
    while(b != 0){
        bi.push(b%2);
        b/=2;
    }
    llint t;
    a%=c;
    llint ans=1;
    while(bi.size()){

        t=bi.front();
        bi.pop();
      
        if(t == 1){
            ans=(ans*a)%c;
        }

        a=(a*a)%c;
    }

    cout<<ans<<'\n';
}
