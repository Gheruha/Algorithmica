/* sorts.hpp - sorts's header file. */
#ifndef sorts_hpp
#define sorts_hpp

#include <vector>
using namespace std;

void sortToExecute(string option);
void display(vector<int> &vec);
void mergeSort(vector<int> &vec);
void merge(vector<int> &leftVec, vector<int> &rightVec, vector<int> &vec);
#endif /* sorts_hpp */
