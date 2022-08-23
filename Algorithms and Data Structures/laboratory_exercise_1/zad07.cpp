#include <iostream>
#include <cmath>
#include <time.h>
using namespace std;

int *funkcija(int polje[], int n)
{
   srand(time(NULL));

   int *B = new int[n];
   int *flagA = new int[n];
   for (int i = 0; i < n; i++)
   {
      int flag = rand() % n;

      while (flagA[flag] == 1)
         flag = rand() % n;

      B[flag] = pow(polje[i], 2.);
      flagA[flag] = 1;
   }

   return B;
}

int main()
{
   int n = 5;
   int *A = (int *)malloc(n * sizeof(int));

   for (int i = 0; i < n; i++)
   {
      cin >> A[i];
   }
   for (int i = 0; i < n; i++)
   {
      cout << A[i] << " ";
   }

   cout << endl;

   A = funkcija(A, n);

   for (int i = 0; i < n; i++)
   {
      cout << A[i] << " ";
   }

   return 0;
   //uvijek pocistit free
}