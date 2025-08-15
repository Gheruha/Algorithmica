/* main.cc - responsible for calling processes from other files. */
#include <iostream>
#include <string>
#include "console/console.hpp"
using namespace std; 

int main(int argc, const char *argv[]){

if (argc < 3) cout << "You need to select 2 options.";
else {
    string option1 = string(argv[1]);
    string option2 = string(argv[2]);
    selectFunction(option1, option2);
  }

}
