// https://atcoder.jp/contests/abc144/tasks/abc144_c

#include <bits/stdc++.h>
#include <list>

using namespace std;

int main() {
  //変数の定義
  long long num, ans=0, x;
  int length;
  vector<int> vec;
  
  //入力を受け取る
  cin >> num;
  
  double a = sqrt(num); 
  for(long i=1;i<=a;i++){ //numの平方根まででループを止める
    if(num%i==0){
      x = i + num/i - 2;
      if(ans==0){
        ans = x;
      }
      if(x<ans){
        ans = x;
     }
   }
  }
 
  //出力
  cout << ans << endl;
}