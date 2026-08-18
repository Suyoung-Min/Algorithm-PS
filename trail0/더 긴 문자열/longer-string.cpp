#include <iostream>
#include <vector>
using namespace std;

int main() {
    string word;
    vector<string> words;
    while(cin>>word){
        words.push_back(word);   
    }
    if(words[0].length()==words[1].length()){
        cout<<"same"<<endl;
    }
    else if(words[0].length()>words[1].length()){
        cout<<words[0]<<" "<<words[0].length()<<endl;
    }
    else{
        cout<<words[1]<<" "<<words[1].length()<<endl;
    }

    return 0;
}