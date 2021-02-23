#include <bits/stdc++.h>
using namespace std;
int main(){
    string s;
    string res = s;
    cin>>s;
    for(int i=0;i<s.size();i++){
        int k = (int)s[i];
        
        if(s[i] > 64 && s[i]< 91){
            if(s.find(s[i]) || s.find((int)s[i]+32)){
                s.erase(s[i]);
                s.erase(s.rfind(s[i]+32))
            }
        }
    }
    return 0;
}