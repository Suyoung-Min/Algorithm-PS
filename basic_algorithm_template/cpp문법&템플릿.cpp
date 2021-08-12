#include <bits/stdc++.h>

using namespace std;

int gcd(int a,int b){
    int c;
    while(b != 0){
        c = a%b;
        a=b;
        b=c;
    }
    return a;
}
/*
유클리드 호제법을 이용한 최대공약수 greater common dividor 계산
*/
int main(){

    int a,b;
    cin>>a>>b;
    cout<<gcd(a,b)<<'\n'<<a*b/gcd(a,b);
    return 0;
}
