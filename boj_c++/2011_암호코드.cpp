#include<iostream>
#include<string>

using namespace std;

int dp[5001];

int main(){

    string str;
    cin>>str;
    dp[0]=1;
    dp[1]=1;

    if(str[0] == '0'){
        cout<<0<<'\n';
        return 0;
    }

    for(int i=1;i<str.length();i++){
        if(str[i] == '0'){
            if(str[i-1] == '1' || str[i-1] == '2'){
                dp[i+1]=dp[i-1];
            }else{
                cout<<0<<'\n';
                return 0;
            }
        }else{
            dp[i+1]=dp[i];
            if(str[i-1] != '0' && ((str[i-1]-'0')*10+(str[i]-'0') <= 26)){
                dp[i+1]=(dp[i+1]+dp[i-1])%1000000;
            }
        }
    }

    cout<<dp[str.length()];
}
