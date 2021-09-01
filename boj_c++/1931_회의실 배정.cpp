#include<iostream>
#include<utility>
#include<algorithm>
using namespace std;

pair<int,int> arr[100001];
int n;
// 회의 종료 시간을 기준으로 
bool compare(const pair<int,int>& a,const pair<int,int>& b){
    if(a.second == b.second){
        return a.first<=b.first;
    }
    return a.second<b.second;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n;

    for(int i=0;i<n;i++){
        cin>>arr[i].first>>arr[i].second;
    }

    sort(arr,arr+n,compare);
  
    int ans=1;
    int prev=arr[0].second;
    for(int i=1;i<n;i++){
        if(arr[i].first >= prev){
            prev=arr[i].second;
            ans++;
        }
    }

    cout<<ans<<'\n';
}
