// https://atcoder.jp/contests/abc142/tasks/abc142_b

#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, k, h, ans=0;
  cin >> n >> k;
  vector<int> height(n);
  
	for (int i=0; i<n; i++){
  	  cin >> height.at(i);
      if(height.at(i)>=k){
        ans += 1;
      }
    }

  cout << ans << endl;
}