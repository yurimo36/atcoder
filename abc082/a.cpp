// https://atcoder.jp/contests/abc082/tasks/abc082_a

#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int x,y,z;
  cin >> x >> y;
  z = x + y;
  
  if (z % 2 == 0){
    cout << z/2 << endl;
  }
  
  else{
    cout << (z+1)/2 << endl;
  }
}

