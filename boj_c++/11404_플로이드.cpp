#include<iostream>
#include<queue>
#include<utility>
#include<algorithm>
using namespace std;

int n,m;
int d[101][101]={0,};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n;
    cin>>m;

    int a,b,c;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(i != j) d[i][j]=int(1e9);
        }
    }

    for(int i=0;i<m;i++){
        cin>>a>>b>>c;
        d[a][b]=min(d[a][b],c);
    }

    for(int t=1;t<=n;t++){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                d[i][j]=min(d[i][j],d[i][t]+d[t][j]);
            }
        }
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(d[i][j] == int(1e9)) d[i][j]=0;
        }
    }

    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cout<<d[i][j]<<' ';
        }
        cout<<'\n';
    }


}
