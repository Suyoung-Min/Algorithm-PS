#include<cstdio>
#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;
using llint=long long;

llint test_gcd(llint a,llint b){
    llint c;
    while(b != 0){
        c=a%b;
        a=b;
        b=c;
    }
    return a;
}
int main(){
    llint gcd,lcm;
    scanf("%lld %lld",&gcd,&lcm);
    
    llint square = gcd*lcm;
    llint min = square+1;
    llint a=gcd,b=lcm;

    for(llint i=gcd;i<=llint(sqrt(square));i+=gcd){
        if(square%i == 0){
            if(square/i + i < min && gcd == test_gcd(i,square/i)){
                a=i;
                b=square/i;
                min = a+b;
            }
        }
    }
    printf("%lld %lld\n",a,b);
}
