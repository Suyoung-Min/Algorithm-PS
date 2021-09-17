#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n,k;
vector<int> d;
vector<int> dist;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n;
    cin>>k;

    d.resize(n);
    dist.resize(n-1);
    for(int i=0;i<n;i++){
        int t;
        cin>>t;
        d[i]=t;
    }
    sort(d.begin(),d.end());
    for(int i=0;i<n-1;i++){
        dist[i]=d[i+1]-d[i];
    }
    sort(dist.begin(),dist.end());
  
    int ans=0;
    for(int i=0;i<n-1-(k-1);i++){
        ans+=dist[i];
    }
    cout<<ans<<'\n';

}
