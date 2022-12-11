//DONE EXTRA: IF STATEMENT, LOOP AND WORKING FUNCTION 
#include <iostream>
#include <cmath> 

//absolute value 
int absolute_value(int v)
{
    return v * ((v > 0) - (v < 0));
}

//basic project
int main() {
  std::cout << "Hello World!\n";
  std::cout <<"-----------------------------------------\n";
  int v = -45;
  std::cout << "absolute value = " << absolute_value(v) << '\n';
  
 std::cout <<"-----------------------------------------\n";  
// if statements to find two numbers is greater
  int x = 20;
  int y = 32;
  if (x == y)
    std::cout << "both are equal"; else if (x > y)
    std::cout << x << " is greater than " << y << '\n';
  else
    std::cout << y << " is greater than " << x << '\n';
   //loop starts 
    
  std::cout <<"-----------------------------------------\n";
  for (int i = 1; i < 10; i ++) {
        std::cout << "The square root of " << i << sqrt(double(i)) << "\n";
    
    }
    
  return 0;
}
