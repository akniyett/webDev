#include <iostream> 
#include <vector> 
using namespace std;

int findTotalWays(vector<long> arr, long i, long k) { 
  
    
    if (k == 0 && i == arr.size()) 
        return 1; 
  
    
    if (i >= arr.size()) 
        return 0; 
  
    
    return findTotalWays(arr, i + 1, k) 
           + findTotalWays(arr, i + 1, k - arr[i]) 
           + findTotalWays(arr, i + 1, k + arr[i]); 
} 
  

int main() 
{ 
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
  
    if(findTotalWays(arr, 0, min)>0) cout<<"Possible";
    else cout<<"Impossible";
  
    return 0; 
} 