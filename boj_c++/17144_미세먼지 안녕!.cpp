#include<iostream>
#include<queue>
#include<utility>
#include<algorithm>
#include<cstdlib>
using namespace std;

typedef struct _cor{
    int y;
    int x;
    int dust;
}cor;

int r,c,t;
int d[51][51]={0,};
int ac1,ac2;

void bfs(){
    queue<cor> q;
    cor tmp;
    for(int i=1;i<=r;i++)
        for(int j=1;j<=c;j++){
            if(d[i][j] != 0 && d[i][j] != -1){
                tmp.y=i,tmp.x=j,tmp.dust=d[i][j];
                q.push(tmp);
            }
        }
    int y,x,dust,diff,diff_num;
    while(q.size()){
        tmp=q.front();
        q.pop();
        y=tmp.y,x=tmp.x,dust=tmp.dust;
        diff=dust/5,diff_num=0;

        if(y-1 >= 1 && d[y-1][x] != -1){
            diff_num++;
            d[y-1][x]+=diff;
        }
        if(y+1<=r && d[y+1][x] != -1){
            diff_num++;
            d[y+1][x]+=diff;
        }
        if(x-1>=1 && d[y][x-1] != -1){
            diff_num++;
            d[y][x-1]+=diff;
        }
        if(x+1<=c && d[y][x+1] != -1){
            diff_num++;
            d[y][x+1]+=diff;
        }

        d[y][x]-=diff*diff_num;
    }
  
    for(int i=ac1-1;i>1;i--) d[i][1]=d[i-1][1];
    for(int i=1;i<c;i++)     d[1][i]=d[1][i+1];
    for(int i=1;i<ac1;i++)   d[i][c]=d[i+1][c];
    for(int i=c;i>2;i--)     d[ac1][i]=d[ac1][i-1];
    d[ac1][2]=0;

    for(int i=ac2+1;i<r;i++) d[i][1]=d[i+1][1];
    for(int i=1;i<c;i++)     d[r][i]=d[r][i+1];
    for(int i=r;i>ac2;i--)   d[i][c]=d[i-1][c];
    for(int i=c;i>2;i--)     d[ac2][i]=d[ac2][i-1];
    d[ac2][2]=0;

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>r>>c>>t;
    for(int i=1;i<=r;i++)
        for(int j=1;j<=c;j++)
            cin>>d[i][j];
    
    ac1=0,ac2=0;
    for(int i=1;i<=r;i++){
        if(d[i][1] == -1){
            if(ac1 == 0){
                ac1 =i;
            }else{
                ac2 = i;
                break;
            }
        }
    }
        
    for(int i=0;i<t;i++){
        bfs();
    }

    int ans=2;
    for(int i=1;i<=r;i++){
        for(int j=1;j<=c;j++)
            ans+=d[i][j];
    }
    cout<<ans<<'\n';
}
