#include <iostream>
#include <cmath>
using namespace std;

double pi(int n)
{
   if (n == 1)
      return 4;
   return pi(n - 1) - 4 * pow(-1, n) / (2 * n - 1);
}
int main()
{
   cout << "Upisite n: ";
   int n;
   cin >> n;
   double *A = new double[n];
   for (int i = 0; i < n; i++)
   {
      A[i] = pi(i + 1);
      cout << A[i] << " ";
   }

   return 0;
}