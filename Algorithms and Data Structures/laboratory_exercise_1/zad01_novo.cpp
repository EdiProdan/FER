#include <iostream>
#include <cmath>
#include <time.h>

using namespace std;

int zbrojiKvadrate(int polje[], int n)
{
   if (n == 0)
      return 0;
   int korijen = sqrt(polje[n - 1]);
   if (korijen * korijen == polje[n - 1])
      return polje[n - 1] + zbrojiKvadrate(polje, n - 1);
   return zbrojiKvadrate(polje, n - 1);
}

int main()
{
   srand(unsigned(time(NULL)));
   int n;
   cout << "n: ";
   cin >> n;

   int *A = new int[n];
   for (int i = 0; i < n; i++)
   {
      A[i] = rand() % 100 + 1;
   }
   for (int i = 0; i < n; i++)
   {
      cout << A[i] << " ";
   }
   cout << endl;
   cout << zbrojiKvadrate(A, n);

   return 0;
}