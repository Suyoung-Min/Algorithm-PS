#include<iostream>
#include<queue>
#include<utility>
#include<algorithm>
#include<cstdlib>
using namespace std;


int n,l,r;
int a[51][51]={0,};
int t[51][51]={0,};
bool visit[51][51]={0,};

void copyTtoA(){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
            a[i][j]=t[i][j];
    }
}

bool bfs(int c,int d){
    queue<pair<int,int>> un;
    queue<pair<int,int>> q;

    int sum=0;
    bool ret;
    un.push(make_pair(c,d));
    q.push(make_pair(c,d));
    visit[c][d]=1;
    sum+=a[c][d];


    pair<int,int> pos;
    int y,x;
    while(q.size()){
        pos=q.front();
        q.pop();

        y=pos.first,x=pos.second;

        if(y-1>=0 && visit[y-1][x] == 0 && ( l <= abs(a[y][x]-a[y-1][x]) ) && (abs(a[y][x]-a[y-1][x]) <= r)){
            visit[y-1][x]=1;
            q.push(make_pair(y-1,x));
            un.push(make_pair(y-1,x));
            sum+=a[y-1][x];
        }
        if(y+1 < n && visit[y+1][x] == 0 && ( l <= abs(a[y][x]-a[y+1][x]) ) && (abs(a[y][x]-a[y+1][x]) <= r)){
            visit[y+1][x]=1;
            q.push(make_pair(y+1,x));
            un.push(make_pair(y+1,x));
            sum+=a[y+1][x];
        }
        if(x-1>=0 && visit[y][x-1] == 0 && ( l <= abs(a[y][x]-a[y][x-1]) ) && (abs(a[y][x]-a[y][x-1]) <= r)){
            visit[y][x-1]=1;
            q.push(make_pair(y,x-1));
            un.push(make_pair(y,x-1));
            sum+=a[y][x-1];
        }
        if(x+1 < n && visit[y][x+1] == 0 && ( l <= abs(a[y][x]-a[y][x+1]) ) && (abs(a[y][x]-a[y][x+1]) <= r)){
            visit[y][x+1]=1;
            q.push(make_pair(y,x+1));
            un.push(make_pair(y,x+1));
            sum+=a[y][x+1];
        }

    }

    sum/=un.size();
    ret = true;
    if(un.size() == 1) ret=false;

    while(un.size()){
        pos=un.front();
        un.pop();

        y=pos.first,x=pos.second;

        t[y][x]=sum;
    }

    return ret;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n>>l>>r;

    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            cin>>a[i][j];
    
    bool flag;
    int time=0;
    while(1){
        flag = false;

        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                visit[i][j]=0;


        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(visit[i][j] == 0){
                    if(bfs(i,j)){
                        flag = true;
                    }
                }
            }
        }

        copyTtoA();

        if(!flag) break; // 인구 이동 발생 x => break

        time++;

    }

    cout<<time<<'\n';
} 
