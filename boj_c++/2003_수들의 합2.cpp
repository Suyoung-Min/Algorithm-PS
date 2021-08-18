#include<iostream>
#include<cstdio>
using namespace std;

int a[10001]={0,};
int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    for(int i=1;i<=n;i++)
        scanf("%d",&a[i]);
    int sum=0,ans=0;
    for(int i=1;i<=n;i++){
        sum=0;
        for(int j=i;j<=n;j++){
            sum+=a[j];
            if(sum == m){
                ans+=1;
                break;
            }
            if(sum > m){
                break;
            }
        }
    }
    printf("%d",ans);
}
