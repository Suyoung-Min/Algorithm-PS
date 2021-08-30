#include<iostream>
using namespace std;

//시간이 오래 걸림, 다른 방식의 dp는? => 일일이 하는 것이 아닌 타겟 좌표의 2x2행렬만 확인하면 됨 by min function

int m,n;
int d[1001][1001]={0,};
int dp[1001][1001]={0,};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>m>>n;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++)
            cin>>d[i][j];
    }


    for(int i=0;i<n;i++){
        if(d[0][i] == 0)
            dp[0][i]=1;
    }
    for(int i=0;i<m;i++){
        if(d[i][0] == 0)
            dp[i][0]=1;
    }

    int t;
    bool break_flag;
    int ans=0;
    for(int i=1;i<m;i++){
        for(int j=1;j<n;j++){
            if(d[i][j] != 0) continue;
            
            t=1;
            break_flag=false;
            dp[i][j]=1;

            while((i-t) >= 0 && (j-t)>= 0){

                for(int r=i-t;r<=i;r++){
                    if(dp[r][j-t] == 0){
                            break_flag = true;
                            break;
                    }
                 }
                

                if(break_flag) break;

                for(int c=j-t;c<=j;c++){
                    if(dp[i-t][c] == 0){
                        break_flag = true;
                        break;
                    }
                }
                if(break_flag) break;
                t++;
            }
            dp[i][j]=t;
        }
    }

    ans=0;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(dp[i][j] > ans) ans = dp[i][j];
        }
    }

    cout<<ans<<'\n';
}

//888ms
##########################################
//68ms

#include<iostream>
#include<algorithm>
using namespace std;

int m,n;
int d[1001][1001]={0,};
int dp[1001][1001]={0,};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>m>>n;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++)
            cin>>d[i][j];
    }


    for(int i=0;i<n;i++){
        if(d[0][i] == 0)
            dp[0][i]=1;
    }
    for(int i=0;i<m;i++){
        if(d[i][0] == 0)
            dp[i][0]=1;
    }

    int t;
    bool break_flag;
    int ans=0;
    for(int i=1;i<m;i++){
        for(int j=1;j<n;j++){
            if(d[i][j] == 0){
                dp[i][j]=min({dp[i-1][j],dp[i-1][j-1],dp[i][j-1]})+1;
            }
        }
    }

    ans=0;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(dp[i][j] > ans) ans = dp[i][j];
        }
    }

    cout<<ans<<'\n';
}
