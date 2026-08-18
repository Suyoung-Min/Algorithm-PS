#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<string> result;
    int score=0;
    cin>>score;
    while(score<=100){
        if(score>=90){
            result.push_back("A");
        }
        else if(score<90 && score>=80){
            result.push_back("B");
        }
        else if(score<80 && score>=70){
            result.push_back("C");
        }
        else if(score<70 && score>=60){
            result.push_back("D");
        }
        else if(score<60){
            result.push_back("F");
        }
        score++;
    }
    for(int i=0; i<result.size(); i++){
        cout<<result[i]<<" ";
    }

    return 0;
}