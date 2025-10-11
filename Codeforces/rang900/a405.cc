/* 405A - Gravity Flip. */
// Solution 1 - using built-in algorithm functions.
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;
  int cube;

  vector<int> cubes;
  for (int i = 0; i < n; ++i) {
    cin >> cube;
    cubes.push_back(cube);
  }

  sort(cubes.begin(), cubes.end());

  for (size_t i = 0; i < cubes.size(); ++i) {
    cout << cubes[i] << " ";
  }
}
