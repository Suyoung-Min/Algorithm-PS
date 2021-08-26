#include<iostream>
#include<queue>
using namespace std;

typedef struct _triple{
    int y;
    int x;
    int l;
}triple;
int d[2188][2188]={0,};
int n;

int chk(int y,int x,int l){
    int tmp=d[y][x];
    bool flag=false;//실패 플래그
    for(int i=y;i<y+l;i++){
        for(int j=x;j<x+l;j++){
            if(d[i][j] != tmp){
                flag=true;
                break;
            }
        }
        if(flag) break;
    }

    if(flag){
        return 2;
    }else{
        return tmp;
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int a=0,b=0,c=0;
    cin>>n;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++)
            cin>>d[i][j];
    }

    queue<triple> q;
    triple t;
    t.y=1,t.x=1,t.l=n;
    q.push(t);
    int y,x,l,tmp;
    while(q.size()){
        t=q.front();
        q.pop();

        y=t.y,x=t.x,l=t.l;
        tmp=chk(y,x,l);
        if(tmp == -1) a++;
        else if(tmp == 0) b++;
        else if(tmp == 1) c++;
        else if(tmp == 2){
            for(int i=y;i<=y+(l/3)*2;i+=(l/3)){
                for(int j=x;j<=x+(l/3)*2;j+=(l/3)){
                    t.y=i,t.x=j,t.l=l/3;
                    q.push(t);
                }
            }
        }
    }
    cout<<a<<'\n';
    cout<<b<<'\n';
    cout<<c<<'\n';
}
