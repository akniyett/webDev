#include <bits/stdc++.h>
using namespace std;
int main(){
    string s;
    cin>>s;
    string res="";
    int c = 0;
    vector<string>v;
    for(int i=0;i<s.size();i++){//YazaAay
        int k = (int)s[i];//97
        // cout<<k<<endl;
        // cout<<(int)res[res.length()-1]<<endl;
        if(res.empty()) res+=s[i];//B
        else if((int)res[res.length()-1] > 64 && (int)res[res.length()-1] < 91){
            if(k == (int)res[res.length()-1] || k == (int)res[res.length()-1]+32){
                res+=s[i];
                v.push_back(res);
            }
            else{
                v.push_back(res);
                res.clear();
                res+=s[i];
            }
            // cout<<1<<" "<<res<<endl;;
        }
        else if((int)res[res.length()-1] > 96 && (int)res[res.length()-1] < 123){
            if(k == (int)res[res.length()-1] || k == (int)res[res.length()-1]-32){
                res+=s[i];
                v.push_back(res);
            }else{
                v.push_back(res);
                res.clear();
                res+=s[i];
            }
            // cout<<2<<" "<<res<<endl;
        }
        else{
            v.push_back(res);
            res.clear();
            res+=s[i];
            // cout<<3<<" "<<res<<endl;
        }

    }
    int max = 0;
    string ans;
    for(int i=0;i<v.size();i++){
        // cout<<v[i]<<" ";
        // if(v[i].size()==max);
        if(v[i].size()>max){
            max=v[i].size();
            ans = v[i];
        }
            
    }
    cout<<ans;
    return 0;
}