#include<iostream>
#include<algorithm>
using namespace std;

int n,m;
int d[500001]={0,};

// https://blog.encrypted.gg/985
int lower_idx(int target){
    int st=0;
    int en=n;
    int mid;
    while(st<en){
        mid=(st+en)/2;
        if(d[mid] >= target) en=mid;
        else st=mid+1;
    }
    return st;
}
int upper_idx(int target){
    int st=0;
    int en=n;
    int mid;
    while(st<en){
        mid=(st+en)/2;
        if(d[mid] > target) en=mid;
        else st=mid+1;
    }
    return st;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n;
    for(int i=0;i<n;i++) cin>>d[i];
    cin>>m;
   
    sort(d,d+n);
    int t;
    while(m--){
        cin>>t;
        cout<<upper_idx(t)-lower_idx(t)<<' ';
    }

}
