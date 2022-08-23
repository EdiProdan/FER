#include <iostream>
using namespace std;

class Stog
{
private:
static const int MAX = 100;
   int *stack;
   int top;

public:
   Stog() : stack(new int[MAX]), top(-1){};
   ~Stog() { delete[] stack; }
   bool push(int element)
   {
      if (top >= MAX)
         return false;
      stack[++top] = element;
      return true;
   }
   void ispis()
   {
      for (int i = 105; i >= 0; i--)
         cout << stack[i] << " ";
   }
};

int main()
{
   srand((unsigned)time(NULL));
   Stog s;
   for (int i = 0; i < 104; i++){
      s.push(rand() % 100);  
   }
   s.ispis();

   return 0;
}