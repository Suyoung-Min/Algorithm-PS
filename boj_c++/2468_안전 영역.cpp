#include<iostream>
#include<cstdio>
#include<utility>
#include<deque>
using namespace std;
/*
방문체크할 때, visit을 true로 체크한 다음 큐에 넣어야 한다. 큐에서 뺀 다음 방문체크하면 메모리 초과
*/
int map[101][101]={0,};
bool visit[101][101]={0,};
int main(){
    int n;
    scanf("%d",&n);
    int min=101,max=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&map[i][j]);
            if(map[i][j] < min) min = map[i][j];
            if(map[i][j] > max) max = map[i][j];
        }
    }

    deque<pair<int,int>> dq;
    pair<int,int> pos;
    int x,y;
    int safe=0,tmp_safe=0;
    for(int t=min-1;t<max;t++){
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                visit[i][j]=false;

        tmp_safe=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(visit[i][j] || map[i][j] <= t) continue;
                tmp_safe++;

                dq.push_back(make_pair(i,j));
                visit[i][j]=true;
                while(dq.size()){
                    pos = dq.front();
                    dq.pop_front();
                    y=pos.first;x=pos.second;
                    visit[y][x] = true;
                    if(y-1 >= 0 && visit[y-1][x] == false && map[y-1][x] > t){
                        dq.push_back(make_pair(y-1,x));
                        visit[y-1][x]=true;
                    }
                    if(y+1 < n && visit[y+1][x] == false && map[y+1][x] > t){
                        dq.push_back(make_pair(y+1,x));
                        visit[y+1][x]=true;
                        }  
                    if(x-1 >= 0 && visit[y][x-1] == false && map[y][x-1] > t){
                        dq.push_back(make_pair(y,x-1));
                        visit[y][x-1]=true;
                        } 
                    if(x+1 < n && visit[y][x+1] == false && map[y][x+1] > t){
                        dq.push_back(make_pair(y,x+1));
                        visit[y][x+1]=true;
                        }  
                }
            }
        }
        if(tmp_safe > safe) safe = tmp_safe;
    }

    printf("%d",safe);
}
