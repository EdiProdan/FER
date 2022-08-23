#include <iostream>
#include <cmath>

using namespace std;

void f(int polje[], int n, int m)
{
   if (n > 0)
   {
      polje[n - 1] = pow(m, n - 1);
      f(polje, n - 1, m);
   }
}

int main()
{
   int n = 10, m = 2;
   int *polje = new int[n];
   f(polje, n, m);
   for (int i = 0; i < n; i++)
   {
      cout << polje[i] << " ";
   }

   return 0;
}