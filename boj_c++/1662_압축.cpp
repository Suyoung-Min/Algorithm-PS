#include<iostream>
#include<string>
#include<stack>
using namespace std;

string s;
int visited[52];

int release(int start,int end){
    int ret=0;

    for(int i=start;i<end;i++){
        if(s[i] == '('){
            int K = s[i-1]-'0';

            ret += K*(release(i+1,visited[i]))-1;
            i=visited[i];

            continue;
        }

        ret++;
    }

    return ret;
}
int main(){

    cin>>s;

    stack<int> st;

    for(int i=0;i<s.length();i++){
        if(s[i] == '('){
            st.push(i);
        }
        else if(s[i] == ')'){
            visited[st.top()]=i;

            st.pop();
        }
    }

    cout<<release(0,s.length())<<'\n';
}
