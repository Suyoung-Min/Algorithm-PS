#include<iostream>
#include<algorithm>
using namespace std;

int n,m;
int arr[9]={0,};
int tmp[9]={0,};
bool visit[9]={0,};

void dfs1(int cnt,int prev){
    if(cnt == m){
        for(int i=0;i<m;i++)
            cout<<tmp[arr[i]-1]<<' ';
        cout<<'\n';
        return;
    }

    for(int i=1;i<=n;i++){
        if(visit[i] == 0){
            visit[i]=true;
            arr[cnt]=i;
            dfs1(cnt+1,i);
            visit[i]=false;
        }
    }
}

int main(){
    cin>>n>>m;
    for(int i=0;i<9;i++){
        tmp[i]=int(1e9);
    }
    for(int i=0;i<n;i++){
        cin>>tmp[i];
    }
    sort(tmp,tmp+9);
    dfs1(0,1);
}
