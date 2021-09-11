#include<iostream>
#include<queue>

using namespace std;

int n;
int d[100001];
bool visit[100001];
int s;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n;
    for(int i=1;i<=n;i++)
        cin>>d[i];

    cin>>s;

    queue<int> q;
    visit[s]=true;
    q.push(s);

    while(!q.empty()){
        int pos = q.front();
        q.pop();

        if(pos+d[pos] <= n && visit[pos+d[pos]] == false){
            visit[pos+d[pos]] = true;
            q.push(pos+d[pos]);
        }
        if(pos-d[pos] >= 1 && visit[pos-d[pos]] == false){
            visit[pos-d[pos]] = true;
            q.push(pos-d[pos]);
        }
    }

    int ans=0;

    for(int i=1;i<=n;i++){
        if(visit[i] == true) ans++;
    }
    cout<<ans<<'\n';
}
