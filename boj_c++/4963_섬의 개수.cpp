#include<iostream>
#include<queue>
#include<algorithm>

using namespace std;


bool d[51][51];
bool visit[51][51];
int dy[8]={-1,-1,-1,0,0,1,1,1};
int dx[8]={-1,0,1,-1,1,-1,0,1};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while(1){
        int w,h;
        cin>>w>>h;

        if(w == 0 && h == 0) break;

        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                cin>>d[i][j];
                visit[i][j]=0;
            }
        }

        
        int ans=0;

        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                if(d[i][j] == 1 && visit[i][j] == false){
                    ans++;
                    visit[i][j]=true;

                    queue<pair<int,int>> q;
                    q.push( {i,j} );

                    while(!q.empty()){
                        int y=q.front().first;
                        int x=q.front().second;
                        q.pop();

                        for(int k=0;k<8;k++){
                            int ty=y+dy[k];
                            int tx=x+dx[k];

                            if(ty < 0 || ty >= h || tx < 0 || tx >= w) continue;

                            if(d[ty][tx] == 1 && visit[ty][tx] == false){
                                visit[ty][tx]=true;
                                q.push( {ty,tx} );
                            }
                        }

                    }
                }
            }
        }

        cout<<ans<<'\n';

    }

}
