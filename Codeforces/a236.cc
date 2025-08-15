/* Problem 236A - Boy or Girl.
 * Done in the easy way, with built in algorithms.
 */
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {

  string s;
  cin >> s;

  vector<char> distinct;
  for (char c : s) {
    if (find(distinct.begin(), distinct.end(), c) == distinct.end())
      distinct.push_back(c);
  }

  if (distinct.size() % 2 == 0)
    cout << "CHAT WITH HER!";
  else
    cout << "IGNORE HIM!";
}
