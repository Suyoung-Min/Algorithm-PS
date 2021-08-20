#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;
using llint =long long;

int A[6][6]={0,};
int C[6][6]={0,};
int tmp[6][6]={0,};
void squareC(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            tmp[i][j]=0;
            for(int k=0;k<n;k++){
                tmp[i][j]+=C[i][k]*C[k][j]%1000;
            }
            tmp[i][j]%=1000;
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
            C[i][j]=tmp[i][j];
    }
}
void mulCA(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            tmp[i][j]=0;
            for(int k=0;k<n;k++){
                tmp[i][j]+=C[i][k]*A[k][j]%1000;
            }
            tmp[i][j]%=1000;
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
            C[i][j]=tmp[i][j];
    }
}
int main(){
    int n;
    llint b;
    string s;
    scanf("%d %lld",&n,&b);

    while(b>1){
        if(b%2 == 1)
            s+='1';
        else
            s+='0';
        b/=2;
    }
    s+='1';
    reverse(s.begin(),s.end());

    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            scanf("%d",&A[i][j]);

    for(int i=0;i<n;i++)
        C[i][i] = 1;
    
    for(int i=0;i<s.size();i++){
        squareC(n);
        if(s[i] == '1')
            mulCA(n);
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
            printf("%d ",C[i][j]);
        printf("\n");
    }
   
}
