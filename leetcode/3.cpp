  
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
string cutall(vector<long>v, long min){
    bool isok = false;
    // long sum = 0;
    // for(long i=0;i<v.size();i++){
    //     sum+=v[i];
    // }
   
    for(long i=0;i<v.size();i++){
        for(int j=0;j<v.size();j++){
            if(v[i]+v[j]==min){
                return "Possible";
                break;
            }
            else if(v[i]+v[j]<min)
        }
        // if(sum-v[i]==min){
        //     isok = true;
        //     break;
        }
        
    }
    if(isok) return "Possible";
    else return "Impossible";
}
int main(){
	long n;
	cin >> n;
	vector<long> arr;
    for(long i=0;i<n;i++){
        long x;
        cin>>x;
        arr.push_back(x);
    }
	long min;
    cin>>min;
    
    cout<<cutall(arr, min);
    
	return 0;
}