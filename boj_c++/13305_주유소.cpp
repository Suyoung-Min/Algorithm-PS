#include<iostream>
using namespace std;
using ll = long long;

ll n;
ll road[100001],oil[100001];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n;
    for(int i=0;i<n-1;i++)
        cin>>road[i];
    for(int i=0;i<n;i++)
        cin>>oil[i];

    ll prev=oil[0];
    ll ans=0;
    for(int i=0;i<=n-2;i++){
        if(prev > oil[i]) prev=oil[i];
        ans+=road[i]*prev;
    }

    cout<<ans<<'\n';
    
}
