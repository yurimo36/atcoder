// https://atcoder.jp/contests/abc144/tasks/abc144_b

#include <bits/stdc++.h>
using namespace std;

int main() {
  int x, y=0;
  cin >> x;
  
  if(x>81){
    cout<< "No" << endl;
  }
  
  else{
  	//判定
  	for(int i=1;i<=9;i++){
      for(int j=1;j<=9;j++){
      	if(i*j==x){
          cout <<"Yes" << endl;
          y = 1;
          break;
        }
      }
      if(y==1){
        break;
      }
    }
    if(y==0){
       cout<< "No" << endl;
    }
  }
}
