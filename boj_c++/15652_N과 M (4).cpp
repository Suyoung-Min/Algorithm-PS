#include<iostream>
using namespace std;

int n,m;
int arr[9]={0,};

void dfs1(int cnt,int prev){
    if(cnt == m){
        for(int i=0;i<m;i++)
            cout<<arr[i]<<' ';
        cout<<'\n';
        return;
    }

    for(int i=prev;i<=n;i++){
            arr[cnt]=i;
            dfs1(cnt+1,i);
    }
}

int main(){
    cin>>n>>m;
    dfs1(0,1);
}
