#include<iostream>
#include<cstdio>
#include<map>
#include<string>
using namespace std;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    map<string,int> npc;
    map<string,int> skku;
    map<string,int>::iterator iter;
    int n;
    string str;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>str;
        if(npc.find(str) != npc.end()){
            iter = npc.find(str);
            iter->second++;
        }
        else{
            npc.insert({str,1});
        }
    }
    for(int i=0;i<n;i++){
        cin>>str;
        if(skku.find(str) != skku.end()){
            iter = skku.find(str);
            iter->second++;
        }
        else{
            skku.insert({str,1});
        }
    }

    int ans=0;
    for(auto t : npc){
        if(skku.find(t.first) != skku.end()){
            iter = skku.find(t.first);
            ans+=min(iter->second,t.second);
        }
    }

    printf("%d\n",ans);
    
}
