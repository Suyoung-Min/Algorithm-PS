#include<stdio.h>
#include<string.h>

int main(){
    char s[52];
    scanf("%s",s);

    int tmp=0;
    int sum=0;
    bool minus=false;

    for(int i=0;i<=strlen(s);i++){
        if(s[i] == '-' || s[i] == '+'){
            if(minus) sum-=tmp;
            else      sum+=tmp;
            tmp=0;
            
            if(s[i] == '-') minus = true;
        }
        else if(i==strlen(s)){
            if(minus) sum-=tmp;
            else      sum+=tmp;
        }
        else{
            tmp*=10;
            tmp+=s[i]-'0';
        }
    }

    printf("%d\n",sum);
}
