/* console.cc - takes the option selected by the user and does the necessary
 * actions. */
#include <iostream>
#include <string>
#include "sorts/sorts.hpp"
using namespace std;

void selectFunction(string &option1, string &option2) {  
  if(option1 == "-sort") sortToExecute(option2); 

}
