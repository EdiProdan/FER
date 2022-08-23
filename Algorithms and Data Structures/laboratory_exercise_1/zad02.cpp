#include <iostream>
#include <cmath>
#include <time.h>

using namespace std;

int zbrojiKvadrate(int polje[], int n)
{
   if (n == 0)
      return 0;

   int sqr = sqrt(polje[n - 1]);
   if (sqr * sqr == polje[n - 1])
      return polje[n - 1] + zbrojiKvadrate(polje, n - 1);

   return zbrojiKvadrate(polje, n - 1);
}

int main()
{
   srand(time(NULL));
   int n;
   cout << "Ucitajte broj elemenata n: ";
   cin >> n;
   int *A = (int *)malloc(n * sizeof(int));

   for (int i = 0; i < n; ++i)
      A[i] = rand() % 100;

   for (int i = 0; i < n; ++i)
      cout << A[i] << " ";
   cout << endl;

   free(A);

   cout << zbrojiKvadrate(A, n);
   return 0;
}
