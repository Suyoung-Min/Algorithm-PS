#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
/*
백만 이하의 자연수가 아니라 백만 자리 이하의 자연수인 것을 명심
*/
int convert(int a){
    int ret=0;
    while(a != 0){
        ret += a%10;
        a/=10;
    }
    return ret;
}
int main(){
    int x=0,ans=0;
    char str[1000002];
    scanf("%s",str);
    if(strlen(str) == 1) x = (str[0]-'0');
    else{
        for(int i=0;i<strlen(str);i++)
            x+=(str[i]-'0');
        ans+=1;
    }

    while(x > 9){
        x = convert(x);
        ans+=1;
    }
    printf("%d\n",ans);
    if(x == 0) printf("NO");
    else if(x%3==0) printf("YES");
    else printf("NO");

    return 0;
}
