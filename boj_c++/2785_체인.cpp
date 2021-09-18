#include<iostream>
#include<queue>
#include<algorithm>
#include<math.h>

using namespace std;

int n;
int d[500001];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n;

    for(int i=0;i<n;i++)
        cin>>d[i];


    sort(d,d+n);

    int basic=n-1;
    int tmp=0;

    for(int i=0;i<n;i++){
        tmp+=d[i];

        if(basic <= tmp){
            break;
        }
        else{
            basic--;
        }
    }

    cout<<basic<<'\n';

}
