#include<iostream>
#include<cstdio>
#include<utility>
#include<deque>
using namespace std;

int visit[301][301]={0,};
int main(){
    int tc;
    scanf("%d",&tc);

    int N;
    int s_y,s_x,t_y,t_x;
    int ans=0;
    deque<pair<int,int>> dq;
    pair<int,int> pos;
    int y,x;

    while(tc--){
        scanf("%d",&N);
        scanf("%d %d",&s_y,&s_x);
        scanf("%d %d",&t_y,&t_x);


        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++)
                visit[i][j]=0;
        }

        ans=0;
        dq.clear();
        dq.push_back(make_pair(s_y,s_x));
        visit[s_y][s_x]=0;
        
        while(dq.size()){
            pos = dq.front();
            dq.pop_front();

            y=pos.first,x=pos.second;

            if((y == t_y) && (x == t_x)){
    
                break;
            }

            if(y-2>=0 && x-1 >= 0 && visit[y-2][x-1] == 0){
                dq.push_back(make_pair(y-2,x-1));
                visit[y-2][x-1]=visit[y][x]+1;
            }
            if(y-2>=0 && x+1 < N && visit[y-2][x+1] == 0){
                dq.push_back(make_pair(y-2,x+1));
                visit[y-2][x+1]=visit[y][x]+1;
            }
            if(y-1>=0 && x-2 >= 0 && visit[y-1][x-2] == 0){
                dq.push_back(make_pair(y-1,x-2));
                visit[y-1][x-2]=visit[y][x]+1;
            }
            if(y-1>=0 && x+2 < N && visit[y-1][x+2] == 0){
                dq.push_back(make_pair(y-1,x+2));
                visit[y-1][x+2]=visit[y][x]+1;
            }
            if(y+2 < N && x-1 >= 0 && visit[y+2][x-1] == 0){
                dq.push_back(make_pair(y+2,x-1));
                visit[y+2][x-1]=visit[y][x]+1;
            }
            if(y+2 < N && x+1 < N && visit[y+2][x+1] == 0){
                dq.push_back(make_pair(y+2,x+1));
                visit[y+2][x+1]=visit[y][x]+1;
            }
            if(y+1 < N && x-2 >= 0 && visit[y+1][x-2] == 0){
                dq.push_back(make_pair(y+1,x-2));
                visit[y+1][x-2]=visit[y][x]+1;
            }
            if(y+1 < N && x+2 < N && visit[y+1][x+2] == 0){
                dq.push_back(make_pair(y+1,x+2));
                visit[y+1][x+2]=visit[y][x]+1;
            }


        }

        printf("%d\n",visit[y][x]);
    }
}
