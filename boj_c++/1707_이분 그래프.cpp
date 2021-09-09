#include<iostream>
#include<string>
#include<vector>
#include<utility>
#include<queue>

using namespace std;

int k;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin>>k;

    while(k--){
        int visit[20001];
        vector<int> d[20001];
        int v,e;
        cin>>v>>e;

        for(int i=0;i<=v;i++) visit[i]=0;

        for(int i=0;i<e;i++){
            int a,b;
            cin>>a>>b;
            d[a].push_back(b);
            d[b].push_back(a);
        }

        for(int i=1;i<=v;i++){
            if(visit[i] == 0){
                queue<int> q;
                q.push(i);
                visit[i]=1;

                while(!q.empty()){
                    int x=q.front();
                    q.pop();

                    int t=visit[x];

                    for(int j=0;j<d[x].size();j++){
                        if(visit[d[x][j]] == 0){
                            if(t == 1){
                                visit[d[x][j]] = 2;
                            }else if(t == 2){
                                visit[d[x][j]] = 1;
                            }
                            q.push(d[x][j]);
                        }
                    }
                }
            }
        }


        bool flag=true;

        for(int i=1;i<=v;i++){
            for(int j=0;j<d[i].size();j++){
                if(visit[i] == visit[d[i][j]]){
                    flag = false;
                    break;
                }
            }
            if(!flag) break;
        }

        if(flag) cout<<"YES\n";
        else     cout<<"NO\n";

    }

}
