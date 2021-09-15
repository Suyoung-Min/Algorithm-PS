#include<iostream>
#include<queue>

using namespace std;
int n,m;
bool num[10];
bool visit0[1000001];
bool visit1[1000001];

typedef struct _tri{
    int x;
    int dist;
    bool flag;
}tri;

int main(){
    cin>>n;
    cin>>m;

    for(int i=0;i<10;i++) num[i]=1;

    for(int i=0;i<m;i++){
        int t;
        cin>>t;
        num[t]=0;
    }

    tri t;
    t.x = 100, t.dist = 0, t.flag = 1; // flag == -,+ 로 넘어가기
    
    visit1[100]=1;
    queue<tri> q;
    q.push(t);

    for(int i=0;i<10;i++){
        if(num[i]){
            visit1[i]=1;
            t.x=i,t.dist=1,t.flag=0;
            q.push(t);
            t.flag=1;
            q.push(t);
        }
    }

    int ans=0;
    while(!q.empty()){
        int x=q.front().x;
        int dist=q.front().dist;
        bool flag=q.front().flag;
        q.pop();

        //printf("x == %d dist == %d\n",x,dist);
        if(x == n){
            ans=dist;
            break;
        }

        if(flag){
            if(x-1 >= 0 && visit0[x-1] == 0 && visit1[x-1] == 0){
                visit1[x-1]=1;
                t.x = x-1, t.dist=dist+1,t.flag=1;
                q.push(t);
            }
            if( (x+1 <= n) && visit0[x+1] == 0 && visit1[x+1] == 0){
                visit1[x+1]=1;
                t.x = x+1,t.dist=dist+1,t.flag=1;
                q.push(t);   
            }
        }else{
            for(int i=0;i<10;i++){
                if(num[i]){
                    if((x*10+i <= 1000000) && visit0[x*10+i] == 0){ 
                        visit0[x*10+i]=1;
                        visit1[x*10+i]=1;
                        t.x = x*10+i,t.dist=dist+1,t.flag=0;
                        q.push(t);
                        t.flag=1;
                        q.push(t);
                    }
                }
            }
        }
    }

    cout<<ans<<'\n';

}
