#include<iostream>
#include<algorithm>

using namespace std;

int r,c;
char d[502][502];
int dy[4]={-1,0,0,1};
int dx[4]={0,-1,1,0};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>r>>c;

    for(int i=0;i<r;i++){
        cin>>d[i];
    }

    bool flag=true;
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if(d[i][j] == 'S'){
                for(int k=0;k<4;k++){
                    int ty=i+dy[k];
                    int tx=j+dx[k];

                    if(ty < 0 || ty >= r || tx < 0 || tx >= c) continue;

                    if(d[ty][tx] == 'W'){
                        flag = false;
                        break;
                    }
                }
                if(!flag) break;
            }
        }
        if(!flag) break;
    }

    if(!flag){
        cout<<0<<'\n';
    }else{
        cout<<1<<'\n';

        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(d[i][j] == 'W'){
                    for(int k=0;k<4;k++){
                        int ty=i+dy[k];
                        int tx=j+dx[k];

                        if(ty < 0 || ty >= r || tx < 0 || tx >= c) continue;

                        if(d[ty][tx] == '.'){
                            d[ty][tx]='D';
                        }
                    }
                }
            }
        }

        for(int i=0;i<r;i++)
            cout<<d[i]<<'\n';

    }
}
