/* Problem 231A - Team */
#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  int s = 0;
  for (int i = 0; i < n; i++) {
    int nr = 0;
    for (int j = 0; j < 3; j++) {
      int x;
      cin >> x;
      nr += x;
    }
    if (nr > 1)
      s++;
  }

  cout << s;
  return 0;
}
