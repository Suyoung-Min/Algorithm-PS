#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

int line[100001][3]={0,};
int main(){
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)   
        scanf("%d %d %d",&line[i][0],&line[i][1],&line[i][2]);
    
    int fir=line[1][0],sec=line[1][1],thd=line[1][2];
    int t_fir,t_sec,t_thd;
    int dmax,dmin;
    for(int i=2;i<=n;i++){
        t_fir = max(fir,sec)+line[i][0];
        t_sec = max({fir,sec,thd})+line[i][1];
        t_thd = max(sec,thd)+line[i][2];
        fir=t_fir;
        sec=t_sec;
        thd=t_thd;
    }
    dmax=max({fir,sec,thd});
    fir=line[1][0],sec=line[1][1],thd=line[1][2];
    for(int i=2;i<=n;i++){
        t_fir = min(fir,sec)+line[i][0];
        t_sec = min({fir,sec,thd})+line[i][1];
        t_thd = min(sec,thd)+line[i][2];
        fir=t_fir;
        sec=t_sec;
        thd=t_thd;
    }
    dmin=min({fir,sec,thd});
    printf("%d %d",dmax,dmin);
}
