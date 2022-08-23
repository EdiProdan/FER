#include <iostream>
#include <cmath>
using namespace std;

double f(double z, int k)
{
   if (k == 0)
   {
      return z;
   }
   else
      
      return (-1) * pow(z, 2.) / ((2 * k + 1) * (2 * k)) * f(z, k - 1);
      return (-1 * pow(z, 2) * f(z, k - 1)) / (((2 * k) + 1) * (2 * k));
}

int main()
{
   double z = 0.5;
   int k = 3;

   cout << f(z, k);

   return 0;
}