#include<iostream>
#include<cstdio>
#include<string>
#include<stack>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string a;
    string b;
    stack<char> ans;
    cin>>a>>b;
    int a_i,b_i;
    int flag=0;
    int ta,tb;
    a_i=a.length()-1;
    b_i=b.length()-1;

    while(1){
        if(a_i == -1 && b_i == -1){
            if(flag == 0)   break;
            ans.push(flag+'0');        
            break;
        }

        if(a_i != -1)
            ta=a[a_i--]-'0';
        else
            ta=0;
        
        if(b_i != -1)
            tb=b[b_i--]-'0';
        else
            tb=0;

        if(ta+tb+flag >= 10){
            ans.push(ta+tb+flag-10+'0');
            flag=1;
        }else{
            ans.push(ta+tb+flag+'0');
            flag=0;
        }
    }

    while(ans.size()){
        cout<<ans.top();
        ans.pop();
    }
}
