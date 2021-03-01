// https://atcoder.jp/contests/abc144/tasks/abc144_a

#include <bits/stdc++.h>
using namespace std;

int main() {
  int x, y;
  cin >> x >> y;
  
  if(x<10&&y<10){
    cout << x*y << endl;
  }
  else
    cout << -1 << endl;
}
