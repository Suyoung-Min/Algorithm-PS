#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;
int n,l;
vector<pair<int,int>> d;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n>>l;
    for(int i=0;i<n;i++){
        int a,b;
        cin>>a>>b;

        d.push_back( {a,b} );
    }
    sort(d.begin(),d.end());

    int prev=0,ans=0;

    for(int i=0;i<n;i++){
        int a=d.front().first;
        int b=d.front().second;
        d.erase(d.begin());

        if(prev >= b) continue;
        if(prev > a) a = prev;
        

        int tmp;
        if((b-a)%l == 0) tmp = (b-a)/l;
        else             tmp = (b-a)/l+1;

        ans+=tmp;
        prev=a+tmp*l;

    }

    cout<<ans<<'\n';
}
