/* main.cc - responsible for calling processes from other files. */
#include <iostream>
#include <string>
#include "console/console.hpp"
using namespace std; 

int main(int argc, const char *argv[]){

if (argc < 2) cout << "You need to select an option.";
else {
    string option = string(argv[1]);
    selectFunction(option);
  }

}
