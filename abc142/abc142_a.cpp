// https://atcoder.jp/contests/abc142/tasks/abc142_a

#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  double ans;
  
  cin >> n;
  
  if(n%2==0){
    ans = 0.5;
  }
  else{
    ans = n - n/2;
    ans = ans / n;
  }
  
  cout << ans << endl;
  
}
