#include<iostream>

using namespace std;

int coin[6]={500,100,50,10,5,1};

int main(){
    int n;
    cin>>n;

    int ans=0;
    int money=1000-n;

    for(int i=0;i<6;i++){
        ans+=money/coin[i];
        money%=coin[i];
    }
    cout<<ans<<'\n';
}
