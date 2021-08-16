#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int w[21][21][21]={0,};
int f(int a,int b,int c){
    if(a<=0 || b<=0 || c<=0) return 1;
    if(a>20 || b>20 || c>20) return f(20,20,20);
    if(w[a][b][c] != 0) return w[a][b][c];

    if(a<b && b<c){
        w[a][b][c] = f(a,b,c-1)+f(a,b-1,c-1)-f(a,b-1,c);
        return w[a][b][c];
    }

    w[a][b][c]= f(a-1,b,c)+f(a-1,b-1,c)+f(a-1,b,c-1)-f(a-1,b-1,c-1);
    return w[a][b][c];
}
int main(){
    int a,b,c;
    while(1){
        scanf("%d %d %d",&a,&b,&c);
        if(a == -1 && b == -1 && c == -1) break;
        printf("w(%d, %d, %d) = %d\n",a,b,c,f(a,b,c));
    }
}
