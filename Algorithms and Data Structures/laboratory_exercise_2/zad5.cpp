#include <iostream>
using namespace std;
class Stog
{
private:
   static const int MAX = 10;
   int *stog;
   int top;

public:
   Stog() : stog(new int[MAX]), top(-1){};
   ~Stog() { delete[] stog; }

   bool push(int element)
   {
      if (top >= MAX)
         return false;

      stog[++top] = element;
      return true;
   }
   bool pop(int &item)
   {
      if (top < 0)
         return false;
      item = stog[top--];
      return true;
   }
};

int main()
{
   Stog s, pom;
   int item;
   srand(unsigned(time(NULL)));
   for (int i = 0; i < 11; i++)
      s.push(rand() % 10 + 1);

   while (s.pop(item))
      pom.push(item);

   while (pom.pop(item))
      cout << item << " ";

   return 0;
}