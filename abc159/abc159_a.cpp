// https://atcoder.jp/contests/abc159/tasks/abc159_a

#include <bits/stdc++.h>
using namespace std;
 
int main(){
  int n, m, ans;
  cin >> n >> m ;
  
  ans = n*(n-1)/2 + m*(m-1)/2;
  
  cout << ans << endl;
}